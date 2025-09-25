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
    freqNormalMin: float = 789.5,
    freqNormalMax: float = 794.5,
    freqShearMin: float = 452.6,
    freqShearMax: float = 457.6,
    delay: float = 1.,
    sampleDrops: int = 3,
    normalPoints: int = 21,
    shearPoints: int = 21
    ) -> list[list[float]]:
    """
    Sweeps through the shear frequencies nested in a sweep of the normal frequencies .\n
    Starts a 2D sweep.

    returns: [[fNormal, normalAmp, normalPha], [fShear, shearAmp, shearPha]]
    """

    optNormal = [freqNormalMin, 0., 180.]
    optShear = [freqShearMin, 0., 180.]

    freqsNormal = np.linspace(freqNormalMin, freqNormalMax, normalPoints, endpoint=True)
    freqsShear = np.linspace(freqShearMin, freqShearMax, shearPoints, endpoint=True)

    for fNormal in freqsNormal:
        print("Normal: "+str(fNormal)+" (Hz)")

        ctrlNormal.Sf(fNormal)

        for fShear in freqsShear:

            ctrlShear.Sf(fShear)
            time.sleep(delay)
            
            try:
                normalAmp = [ctrlNormal.Rm() for _ in range(sampleDrops+1)][-1]
            except:
                normalAmp = np.nan

            try:
                normalPha = [ctrlNormal.Rp() for _ in range(sampleDrops+1)][-1]
            except:
                normalPha = np.nan

            try:
                shearAmp = [ctrlShear.Rm() for _ in range(sampleDrops+1)][-1]
            except:
                shearAmp = np.nan

            try:
                shearPha = [ctrlShear.Rp() for _ in range(sampleDrops+1)][-1]
            except:
                shearPha = np.nan                
            
            if normalAmp >= optNormal[1] and normalPha <= optNormal[2] and shearAmp >= optShear[1] and shearPha <= optShear[2]:
                optNormal = [fNormal, normalAmp, normalPha]
                optShear = [fShear, shearAmp, shearPha]

    return [optNormal, optShear]

def PLL2x1D(
    ctrlNormal: sfa.sfa,
    ctrlShear: sfa.sfa,
    freqNormalMin: float = 789.5,
    freqNormalMax: float = 794.5,
    freqShearMin: float = 452.6,
    freqShearMax: float = 457.6,
    delay: float = 1.,
    sampleDrops: int = 3,
    normalPoints: int = 21,
    shearPoints: int = 21
    ) -> list[list[float]]:
    """
    Sweeps through normal frequencies and the shear frequencies sequentially.\n
    Creates 2 1D sweeps, instead of a full 2D sweep.

    returns: [[fNormal, normalAmp, normalPha], [fShear, shearAmp, shearPha]]
    """

    optNormal = [freqNormalMin, 0., 180.]
    optShear = [freqShearMin, 0., 180.]

    freqsNormal = np.linspace(freqNormalMin, freqNormalMax, normalPoints, endpoint=True)
    freqsShear = np.linspace(freqShearMin, freqShearMax, shearPoints, endpoint=True)

    for fNormal in freqsNormal:
        ctrlNormal.Sf(fNormal)
        print("Normal: "+str(fNormal)+" (Hz)")
        time.sleep(delay)
        try:
            normalAmp = [ctrlNormal.Rm() for _ in range(sampleDrops+1)][-1]
        except:
            normalAmp = np.nan

        try:
            normalPha = [ctrlNormal.Rp() for _ in range(sampleDrops+1)][-1]
        except:
            normalPha = np.nan

        if normalAmp >= optNormal[1] and normalPha <= optNormal[2]:
            optNormal = [fNormal, normalAmp, normalPha]

    for fShear in freqsShear:
        ctrlShear.Sf(fShear)
        print("Shear: "+str(fNormal)+" (Hz)")
        time.sleep(delay)

        try:
            shearAmp = [ctrlShear.Rm() for _ in range(sampleDrops+1)][-1]
        except:
            shearAmp = np.nan

        try:
            shearPha = [ctrlShear.Rp() for _ in range(sampleDrops+1)][-1]
        except:
            shearPha = np.nan

        if shearAmp >= optShear[1] and shearPha <= optShear[2]:
            optShear = [fShear, shearAmp, shearPha]

    return [optNormal, optShear]


if __name__ == "__main__":
    # Create an instance of the sfa class.
    controller = sfa.sfa()

    # Run the PLL routine to estimate the resonance frequency.
    resonance_freq = PLL1D(controller, gamma=15)
    print(f"Final estimated resonance frequency: {resonance_freq:.6f} Hz")

    # Close the serial connection.
    controller.ser.close()
