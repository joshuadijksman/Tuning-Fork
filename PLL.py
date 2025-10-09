"""
Phase Lock Loop

Sweeps through the frequencies, while recording amplitudes and phase of the returning wave.
At resonance, the amplitude will be greatest and the phase shift at 0.
"""

import numpy as np
import time
from newsfa import sfa  # Ensure sfa.py is in the same directory
from rigol_dg1022 import RigolDG

def PLL1D(
    ctrl: sfa,
    freqGen: RigolDG,
    freqMin: int | float,
    freqMax: int | float,
    points: int = 11,
    tolerance: int | float = 1e-3,
    iterations: int = 20, 
    freqGenChannel: int = 1,
    Kp=1/(np.pi),
    delay: float = 0.75,
    sampleDrops: int = 3
    ) -> list[float]:
    """
    Find the resonance frequency using a PLL approach via the sfa controller.

    The amplitude sweep uses the measured amplitude (Rm) to pick an initial guess.
    The PLL loop reads the phase (Rp) and converts it to radians. Resonance is
    defined as when the phase error is near zero.

    :returns: [fRes, ampRes, phaRes]
    :rtype: list[float]
    """
    freqs = np.linspace(freqMin, freqMax, points)
    amplitudes = np.zeros_like(freqs)

    for i, f in enumerate(freqs):
        freqGen.set_frequency(freqGenChannel, f)
        time.sleep(delay)

        amp = ctrl.readAmplitude()

        amplitudes[i] = amp

    best_index = np.argmax(amplitudes)
    fRes: float = freqs[best_index]
    print(f"Initial guess from amplitude sweep: {fRes:.3f} Hz")

    freqGen.set_frequency(freqGenChannel, fRes)
    time.sleep(delay)

    phaseDeg = ctrl.readPhase()

    print(f"Iteration -1: Frequency = {fRes:.6f} Hz, "
            f"Phase = {phaseDeg:.2f} deg")

    if abs(np.deg2rad(phaseDeg)) < tolerance:
         return [fRes, ctrl.readAmplitude(), phaseDeg]
    
    fPrev = fRes
    phasePrev = phaseDeg
    fRes = fRes + Kp * np.deg2rad(phaseDeg)
    
    for i in range(iterations):
        freqGen.set_frequency(freqGenChannel, fRes)
        time.sleep(delay)

        phaseDeg = ctrl.readPhase()

        print(f"Iteration {i:3d}: Frequency = {fRes:.6f} Hz, "
            f"Phase = {phaseDeg:.2f} deg")

        if abs(np.deg2rad(phaseDeg)) < tolerance:
            if phaseDeg * phasePrev < 0:
                f_interp = fPrev - phasePrev*(fPrev-fRes)/(phasePrev-phaseDeg)
                print(f"  → Interpolated f_res = {f_interp:.6f} Hz")
                return [f_interp, ctrl.readAmplitude(), phaseDeg]
                
        # TODO: REVIEW THIS PART, FROM OLD "NEW" CODE. SUSPICION: WILL ALWAYS DEFAULT WHEN PHASE IS NEGATIVE, INC -180
        if phasePrev * phaseDeg < 0:
            f_interp = fPrev - phasePrev*(fRes-fPrev)/(phaseDeg-phasePrev)
            print(f"  → Sign change, interpolated f_res = {f_interp:.6f} Hz")
            return [f_interp, ctrl.readAmplitude(), phaseDeg]
        
        fPrev = fRes
        phasePrev = phaseDeg
        fRes = fRes + Kp * np.deg2rad(phaseDeg)

    else:
        opt = [fRes, ctrl.readAmplitude(), phaseDeg]
        print("Maximum iterations reached without full convergence in the PLL loop.")

    return opt


def PLL2D(
    ctrlNormal: sfa,
    ctrlShear: sfa,
    freqGen: RigolDG,
    freqNormalRange: list[int | float] = [789.5, 794.5],
    freqShearRange: list[int | float] = [452.6, 457.6],
    delay: int | float = 0.75,
    iterations: int = 3,
    Kp: float = 1 / (np.pi),
    tolerance: float = 1e-3,
    sampleDrops: int = 3,
    points: list[int] = [6, 6],
    ) -> list[list[float]]:
    """
    Sweeps through the shear frequencies nested in a sweep of the normal frequencies .\n
    Starts a 2D sweep. At worst O(n^2) time complexity.

    :returns: [[fNormal, normalAmp, normalPha], [fShear, shearAmp, shearPha]] 
    :rtype: list[list[float]]

    """

    optNormal: list[float] = [freqNormalRange[0], 0., 180.]
    optShear: list[float] = [freqShearRange[0], 0., 180.]

    freqsNormal = np.linspace(*freqNormalRange, num=points[0], endpoint=True)
    freqsShear = np.linspace(*freqShearRange, num=points[1], endpoint=True)

    amps = np.zeros(shape=(points[0], points[1]))

    for i, fNormal in enumerate(freqsNormal.data):
        freqGen.set_frequency(1, fNormal)

        for j, fShear in enumerate(freqsShear.data):
            freqGen.set_frequency(2, fShear)
            time.sleep(delay)

            amps[i, j] = np.sqrt((ctrlNormal.readAmplitude()**2)/2 +
                                 (ctrlNormal.readAmplitude()**2)/2)

    indAmp = np.unravel_index(np.argmax(amps), amps.shape)
    fResNormal: float = freqsNormal[indAmp[0]]
    fResShear: float = freqsShear[indAmp[1]]
    print(
        f"Initial guess from amplitude sweep: \n Normal: {fResNormal:.3f} Hz\nShear: {fResShear:.3f} Hz")

    # Normal loop
    for i in range(iterations):
        freqGen.set_frequency(1, fResNormal)

        # Shear loop
        for j in range(iterations):
            freqGen.set_frequency(2, fResShear)
            time.sleep(delay)

            phaseDegShear = ctrlShear.readPhase()

            print(f"Iteration {j:3d}: Frequency = {fResShear:.6f} Hz, "
                  f"Phase = {phaseDegShear:.2f} deg")

            if abs(np.deg2rad(phaseDegShear)) < tolerance:
                print(
                    f"(Shear) PLL converged after {j} iterations with frequency {fResShear:.6f} Hz")
                optShear = [fResShear, ctrlShear.readAmplitude(), phaseDegShear]
                break

            fResShear = fResShear + Kp * np.deg2rad(phaseDegShear)

        else:
            optShear = [fResShear, ctrlShear.readAmplitude(), phaseDegShear]
            print(
                "(Shear) Maximum iterations reached without full convergence in the PLL loop.")
        # End shear loop

        try:
            phaseDegNormal = ctrlNormal.readPhase()
        except:
            phaseDegNormal = 180.0

        print(f"Iteration {i:3d}: Frequency = {fResNormal:.6f} Hz, "
              f"Phase = {phaseDegNormal:.2f} deg")

        if abs(np.deg2rad(phaseDegNormal)) < tolerance:
            print(
                f"(Normal) PLL converged after {i} iterations with frequency {fResNormal:.6f} Hz")
            optNormal = [fResNormal, ctrlNormal.readAmplitude(), phaseDegNormal]
            break

        fResNormal = fResNormal + Kp * np.deg2rad(phaseDegNormal)
    else:
        optNormal = [fResNormal, ctrlNormal.readAmplitude(), phaseDegNormal]
        print(
            "(Normal) Maximum iterations reached without full convergence in the PLL loop.")

    return [optNormal, optShear]


def PLL2x1D(
    ctrlNormal: sfa,
    ctrlShear: sfa,
    freqGen: RigolDG,
    freqNormalRange: list[int | float] = [789.5, 794.5],
    freqShearRange: list[int | float] = [452.6, 457.6],
    points: list[int] = [6, 6],
    tolerance: float = 1e-3,
    Kp: float = 15 / (4 * np.pi),
    iterations: int = 3,
    delay: int | float = 0.75,
    sampleDrops: int = 3
    ) -> list[list[float]]:
    """
    Sweeps through normal frequencies and the shear frequencies sequentially.\n
    Starts 2 seperate 1D sweeps, instead of the full 2D sweep. O(n) time complexity.

    (This function is twice PLL1D in disguise)

    :returns: [[fNormal, normalAmp, normalPha], [fShear, shearAmp, shearPha]]
    :rtype: list[list[float]]
    """

    optNormal = PLL1D(
        ctrlNormal,
        freqGen,
        freqNormalRange[0],
        freqNormalRange[1],
        points[0],
        freqGenChannel=1,
        tolerance=tolerance,
        iterations=iterations,
        Kp=Kp,
        delay=delay,
        sampleDrops=sampleDrops
    )
    optShear = PLL1D(
        ctrlShear,
        freqGen,
        freqShearRange[0],
        freqShearRange[1],
        points[1],
        freqGenChannel=2,
        tolerance=tolerance,
        iterations=iterations,
        Kp=Kp,
        delay=delay,
        sampleDrops=sampleDrops
    )

    return [optNormal, optShear]


if __name__ == "__main__":
    # Create an instance of the sfa class.
    ctrlNormal = sfa(SN="")
    freqGen = RigolDG()
    freqGen.set_waveform(1, "SIN")
    freqGen.set_waveform(2, "SIN")
    freqGen.set_output(1, True)
    freqGen.set_output(2, True)
    # Run the PLL routine to estimate the resonance frequency.
    resonance_freq = PLL1D(ctrlNormal, freqGen, 789.5, 794.5)
    print(f"Final estimated resonance frequency: {resonance_freq:.6f} Hz")

    # Close the serial connection.
    ctrlNormal.ser.close()
