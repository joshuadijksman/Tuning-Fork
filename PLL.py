"""
Phase Lock Loop

Sweeps through the frequencies, while recording amplitudes and phase of the returning wave.
At resonance, the amplitude will be greatest and the phase shift at 0.
"""

import numpy as np
import time
import newsfa as sfa  # Ensure sfa.py is in the same directory


def PLL1D(controller: sfa.sfa,
          freq_min=750,
          freq_max=840,
          sweep_points=20,
          tol=1e-3,
          max_iterations=25,
          gamma=15,
          delay: float = 0.75
          ):
    """
    Find the resonance frequency using a PLL approach via the sfa controller.

    The amplitude sweep uses the measured amplitude (Rm) to pick an initial guess.
    The PLL loop reads the phase (Rp) and converts it to radians. Resonance is
    defined as when the phase error is near zero.
    """
    # 1. Amplitude sweep using measured amplitude (Rm).
    freqs = np.linspace(freq_min, freq_max, sweep_points)
    amplitudes = []

    for f in freqs:
        controller.Sf(f)
        time.sleep(delay)  # Amplitude measurement delay

        try:
            amp = controller.Rm()
        except:
            amp = 0.

        amplitudes.append(amp)
    amplitudes = np.array(amplitudes)
    best_index = np.argmax(amplitudes)
    f_res_guess = freqs[best_index]
    current_freq = f_res_guess
    print(f"Initial guess from amplitude sweep: {current_freq:.3f} Hz")

    # Proportional gain (gamma = guess atm!)
    Kp = gamma / (4 * np.pi)
    print(f"Using proportional gain: Kp = {Kp:.5f} Hz per radian")

    # 2. PLL loop
    for i in range(max_iterations):
        controller.Sf(current_freq)
        time.sleep(delay)  # Phase measurement delay

        try:
            measured_phase_deg = controller.Rp()
        except:
            measured_phase_deg = 0.0

        # Convert phase to radians
        error = np.deg2rad(measured_phase_deg)
        print(f"Iteration {i:3d}: Frequency = {current_freq:.6f} Hz, "
              f"Phase = {measured_phase_deg:.2f} deg, "
              f"Phase error = {error:.6f} rad")

        # Check error tolerance
        if abs(error) < tol:
            print(
                f"PLL converged after {i} iterations with frequency {current_freq:.6f} Hz")
            break

        # Update the frequency using the error
        current_freq = current_freq + Kp * error
    else:
        print("Maximum iterations reached without full convergence in the PLL loop.")

    return current_freq


def PLL2D(
    ctrlNormal: sfa.sfa,
    ctrlShear: sfa.sfa,
    freqNormalRange: list[int | float] = [789.5, 794.5],
    freqShearRange: list[int | float] = [452.6, 457.6],
    delay: int | float = 0.75,
    iterations: int = 3,
    Kp: float = 15 / (4 * np.pi),
    tolerance: float = 1e-3,
    sampleDrops: int = 3,
    points: list[int] = [6, 6],
    ) -> list[list[float]]:
    """
    Sweeps through the shear frequencies nested in a sweep of the normal frequencies .\n
    Starts a 2D sweep. At worst O(n^2) time complexity.

    returns: [[fNormal, normalAmp, normalPha], [fShear, shearAmp, shearPha]]
    """

    optNormal = [freqNormalRange[0], 0., 180.]
    optShear = [freqShearRange[0], 0., 180.]

    freqsNormal = np.linspace(*freqNormalRange, num=points[0], endpoint=True)
    freqsShear = np.linspace(*freqShearRange, num=points[1], endpoint=True)

    amps = np.zeros(shape=(points[0], points[1]))

    for i, fNormal in enumerate(freqsNormal.data):
        ctrlNormal.Sf(fNormal)

        for j, fShear in enumerate(freqsShear.data):
            ctrlShear.Sf(fShear)
            time.sleep(delay)

            try:
                amps[i,j] = np.sqrt(([ctrlNormal.Rm() for _ in range(sampleDrops+1)][-1]**2)/2 + \
                                    ([ctrlNormal.Rm() for _ in range(sampleDrops+1)][-1]**2)/2)
            except:
                amps[i,j] = np.nan

    indAmp = np.unravel_index(np.argmax(amps), amps.shape)
    fResNormal: int | float = freqsNormal[indAmp[0]]
    fResShear: int | float = freqsShear[indAmp[1]]
    print(f"Initial guess from amplitude sweep: \n Normal: {fResNormal:.3f} Hz\nShear: {fResShear:.3f} Hz")

    # Normal loop
    for i in range(iterations):
        ctrlNormal.Sf(fResNormal)
        
        # Shear loop
        for j in range(iterations):
            ctrlShear.Sf(fResShear)
            time.sleep(delay)

            try:
                phaseDegShear = [ctrlShear.Rp() for _ in range(sampleDrops+1)][-1]
            except:
                phaseDegShear = 180.0

            print(f"Iteration {j:3d}: Frequency = {fResShear:.6f} Hz, "
                f"Phase = {phaseDegShear:.2f} deg")

            if abs(np.deg2rad(phaseDegShear)) < tolerance:
                print(f"(Shear) PLL converged after {j} iterations with frequency {fResShear:.6f} Hz")
                optShear = [fResShear, [ctrlShear.Rm() for _ in range(sampleDrops+1)][-1], phaseDegShear]
                break

            fResShear = fResShear + Kp * np.deg2rad(phaseDegShear)

        else:
            optShear = [fResShear, [ctrlShear.Rm() for _ in range(sampleDrops+1)][-1], phaseDegShear]
            print("(Shear) Maximum iterations reached without full convergence in the PLL loop.")
        # End shear loop

        try:
            phaseDegNormal = [ctrlNormal.Rp() for _ in range(sampleDrops+1)][-1]
        except:
            phaseDegNormal = 180.0

        print(f"Iteration {i:3d}: Frequency = {fResNormal:.6f} Hz, "
              f"Phase = {phaseDegNormal:.2f} deg")

        if abs(np.deg2rad(phaseDegNormal)) < tolerance:
            print(f"(Normal) PLL converged after {i} iterations with frequency {fResNormal:.6f} Hz")
            optNormal = [fResNormal, [ctrlNormal.Rm() for _ in range(sampleDrops+1)][-1], phaseDegNormal]
            break

        fResNormal = fResNormal + Kp * np.deg2rad(phaseDegNormal)
    else:
        optNormal = [fResNormal, [ctrlNormal.Rm() for _ in range(sampleDrops+1)][-1], phaseDegNormal]
        print("(Normal) Maximum iterations reached without full convergence in the PLL loop.")


    return [optNormal, optShear]

def PLL2x1D(
    ctrlNormal: sfa.sfa,
    ctrlShear: sfa.sfa,
    freqNormalRange: list[int | float] = [789.5, 794.5],
    freqShearRange: list[int | float] = [452.6, 457.6],
    delay: int | float = 0.75,
    iterations: int = 3,
    Kp: float = 15 / (4 * np.pi),
    tolerance: float = 1e-3,
    sampleDrops: int = 3,
    points: list[int] = [6, 6],
    ) -> list[list[float]]:
    """
    Sweeps through normal frequencies and the shear frequencies sequentially.\n
    Starts 2 seperate 1D sweeps, instead of the full 2D sweep. O(n) time complexity.

    returns: [[fNormal, normalAmp, normalPha], [fShear, shearAmp, shearPha]]
    """

    optNormal = [freqNormalRange[0], 0., 180.]
    optShear = [freqShearRange[0], 0., 180.]

    freqsNormal = np.linspace(*freqNormalRange, num=points[0], endpoint=True)
    freqsShear = np.linspace(*freqShearRange, num=points[1], endpoint=True)

    ampNormal = np.zeros_like(freqsNormal)
    ampShear = np.zeros_like(freqsShear)

    for i, fNormal in enumerate(freqsNormal.data):
        ctrlNormal.Sf(fNormal)
        time.sleep(delay)
        try:
            ampNormal[i] = [ctrlNormal.Rm() for _ in range(sampleDrops+1)][-1]
        except:
            ampNormal[i] = np.nan

    for i, fShear in enumerate(freqsShear.data):
        ctrlShear.Sf(fShear)
        time.sleep(delay)
        try:
            ampShear[i] = [ctrlShear.Rm() for _ in range(sampleDrops+1)][-1]
        except:
            ampShear[i] = np.nan

    fResNormal = freqsNormal[np.argmax(ampNormal)]
    fResShear = freqsShear[np.argmax(ampShear)]
    print(f"Initial guess from amplitude sweep: \n Normal: {fResNormal:.3f} Hz\nShear: {fResShear:.3f} Hz")

    for i in range(iterations):
        ctrlNormal.Sf(fResNormal)
        time.sleep(delay)  # Phase measurement delay

        try:
            phaseDeg = [ctrlNormal.Rp() for _ in range(sampleDrops+1)][-1]
        except:
            phaseDeg = 180.0

        print(f"Iteration {i:3d}: Frequency = {fResNormal:.6f} Hz, "
              f"Phase = {phaseDeg:.2f} deg")

        if abs(np.deg2rad(phaseDeg)) < tolerance:
            print(f"(Normal) PLL converged after {i} iterations with frequency {fResNormal:.6f} Hz")
            optNormal = [fResNormal, [ctrlNormal.Rm() for _ in range(sampleDrops+1)][-1], phaseDeg]
            break

        fResNormal = fResNormal + Kp * np.deg2rad(phaseDeg)
    else:
        optNormal = [fResNormal, [ctrlNormal.Rm() for _ in range(sampleDrops+1)][-1], phaseDeg]
        print("(Normal) Maximum iterations reached without full convergence in the PLL loop.")

    
    for i in range(iterations):
        ctrlShear.Sf(fResShear)
        time.sleep(delay)  # Phase measurement delay

        try:
            phaseDeg = [ctrlShear.Rp() for _ in range(sampleDrops+1)][-1]
        except:
            phaseDeg = 180.0

        print(f"Iteration {i:3d}: Frequency = {fResShear:.6f} Hz, "
              f"Phase = {phaseDeg:.2f} deg")

        # Check error tolerance
        if abs(np.deg2rad(phaseDeg)) < tolerance:
            print(f"(Shear) PLL converged after {i} iterations with frequency {fResShear:.6f} Hz")
            optShear = [fResShear, [ctrlShear.Rm() for _ in range(sampleDrops+1)][-1], phaseDeg]
            break

        # Update the frequency using the error
        fResShear = fResShear + Kp * np.deg2rad(phaseDeg)
    else:
        optShear = [fResShear, [ctrlShear.Rm() for _ in range(sampleDrops+1)][-1], phaseDeg]
        print("(Shear) Maximum iterations reached without full convergence in the PLL loop.")


    return [optNormal, optShear]


if __name__ == "__main__":
    # Create an instance of the sfa class.
    ctrlNormal = sfa.sfa(PID=0x7523, VID=0x1A86)

    # Run the PLL routine to estimate the resonance frequency.
    resonance_freq = PLL1D(ctrlNormal, gamma=15)
    print(f"Final estimated resonance frequency: {resonance_freq:.6f} Hz")

    # Close the serial connection.
    ctrlNormal.ser.close()
