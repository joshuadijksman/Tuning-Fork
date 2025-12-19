from scipy.optimize import curve_fit
import time
import pandas as pd
import numpy as np
from rigol_dg1022 import RigolDG

from pi_e_625 import pi_e_625
from mitutoyo import mitutoyo
from newsfa import sfa
import PLL


def calibrateAirSingle(
    ctrl: sfa,
    freqGen: RigolDG,
    freqGenChannel: int,
    freqMin: float = 789.5,
    freqMax: float = 794.5,
    delay: float = 0.75,
    denseHalfwidth: float = 3.0,
    denseStep: float = 0.1,
    fitMaxFev: float = 5000,
    accelerometerGConversion: float = 0.66,
    **kwargs,
) -> list[float]:
    """
    Calibration module for C0 and \u03b3 system, designed for air.

    Seeks resonance frequency in range `freqMin` to `freqMax` and does a sweep with stepsize `denseStep` for a region `-denseHalfwidth` and `+denseHalfwidth` around the resonance frequency.\\
    After the dense sweep a fit will be made, which extracts the values for C0 and \u03b3 system.

    :param ctrl: Lock-In Amplifier controller.
    :type ctrl: sfa

    :param freqGen: Frequency Generator to use.
    :type freqGen: RigolDG

    :param freqGenChannel: Channel on frequency generator to use.
    :type freqGenChannel: int

    :param freqMin: Start of initial guess range. default: `789.5` Hz
    :type freqMin: float

    :param freqMax: End of inititial guess range. default: `794.5` Hz
    :type freqMax: float

    :param delay: Delay between setting the new frequency and measuring the amplitude. default: `0.75` s
    :type delay: float

    :param denseHalfwidth: Width of densesweep from resonance frequency. default: `3.0` Hz
    :type denseHalfwidth: float

    :param denseStep: Frequency step size used in dense sweep. default: `0.1` Hz
    :type denseStep: float

    :param fitMaxFev: Maximum Fev value for scipy fit. default: `5000`
    :type fitMaxFev: float

    :param accelerometerGConversion: Conversionvalue for accelerometer voltage to g. default: `0.66` V/g
    :type accelerometerGConversion: float

    :param points: How many points to use in coarse sweep. default: `7`
    :type points: int

    :param tolerance: What phase angle is ''good enough''. default: `0.1/180 * \u03c0` RAD
    :type tolerance: float

    :param iterations: Maximum iterations the PLL tries to converge. default: `5`
    :type iterations: int

    :param Kp: Kp value for PLL loop. default: `4 / \u03c0'
    :type Kp: float

    :param debugPrints: How much should be printed to console `['all', 'results', 'none']`, default: 'results'
    :type debugPrints: str

    :returns: [fRes, ampRes, phaRes]
    :rtype: list[float]
    """
    debugPrints: str = kwargs.get("debugPrints", "results")
    g = 9.81

    optimalPLL = PLL.PLL1D(
        ctrl=ctrl,
        freqGen=freqGen,
        freqGenChannel=freqGenChannel,
        freqMin=freqMin,
        freqMax=freqMax,
        delay=delay,
        points=kwargs.get("points", 7),
        tolerance=kwargs.get("tolerance", (0.1 / 180) * np.pi),
        iterations=kwargs.get("iterations", 5),
        Kp=kwargs.get("Kp", 4 / np.pi),
        debugPrint=True if debugPrints.lower() in ["all"] else False,
    )

    fResonance = optimalPLL[0]

    numPts = int(round((2 * denseHalfwidth) / denseStep)) + 1
    freqsDense = np.linspace(
        fResonance - denseHalfwidth, fResonance + denseHalfwidth, numPts
    )
    ampsDense = np.empty_like(freqsDense)
    phasesDense = np.empty_like(freqsDense)

    for i, f in enumerate(freqsDense):
        freqGen.set_frequency(freqGenChannel, f)
        time.sleep(delay)
        ampsDense[i] = ctrl.readAmplitude()
        phasesDense[i] = ctrl.readPhase()
        if debugPrints in ["all", "results"]:
            print(
                f"[CAL] Dense sweep: f={f:.3f} Hz, A={ampsDense[i]:.6f}, φ={phasesDense[i]:.2f}"
            )

    # fit Lorentzian
    ω0Normal = 2 * np.pi * fResonance
    ampsMeters = (ampsDense * accelerometerGConversion) * g
    C0Normal = np.nanmax(ampsMeters) * ω0Normal
    gamma0Normal = ω0Normal / 10.0

    def A_model(f, C, gamma_sys, omega0):
        ω = 2 * np.pi * f
        return C / np.sqrt((omega0**2 - ω**2) ** 2 + (gamma_sys * ω) ** 2)

    poptNormal, _ = curve_fit(
        A_model,
        freqsDense,
        ampsMeters,
        p0=[C0Normal, gamma0Normal, ω0Normal],
        bounds=([0, 0, 0], [np.inf, np.inf, np.inf]),
        nan_policy="omit",
        maxfev=fitMaxFev,
    )
    CNormal, gammaNormal, omega0Normal = poptNormal
    f0Normal = omega0Normal / (2 * np.pi)
    if debugPrints in ["all", "results"]:
        print(
            f"[CAL] (Normal) Fit results: f_res={f0Normal:.6f} Hz, C={CNormal:.3e}, γ_sys={gammaNormal:.3e}"
        )

    return [f0Normal, CNormal, gammaNormal]


def calibrateAir(
    ctrlNormal: sfa,
    ctrlShear: sfa,
    freqGen: RigolDG,
    freqNormalRange: list[float] = [789.5, 794.5],
    freqShearRange: list[float] = [452.6, 457.6],
    delay: float = 0.75,
    denseHalfwidth: float = 3.0,
    denseStep: float = 0.1,
    fitMaxFev: float = 5000,
    accelerometerGConversion: float = 0.66,
    **kwargs,
) -> tuple[list[float], list[float]]:
    """
    Calibration module for C0 and \u03b3 system, designed for air.

    Difference with calibrateAirSingle: sweeps over both Normal and Shear mode.
    Seeks resonance frequency in range `freq...Range[0]` to `freq...Range[1]` and does a sweep with stepsize `denseStep` for a region `-denseHalfwidth` and `+denseHalfwidth` around the resonance frequency.\\
    After the dense sweep a fit will be made, which extracts the values for C0 and \u03b3 system.

    :param ctrlNormal: Lock-In Amplifier controller for the Normal mode.
    :type ctrlNormal: sfa

    :param ctrlShear: Lock-In Amplifier controller for the Shear mode.
    :type ctrlShear: sfa

    :param freqGen: Frequency Generator to use.
    :type freqGen: RigolDG

    :param freqNormalRange: Start and end of initial guess range. default: `[789.5, 794.5]` Hz
    :type freqNormalRange: list[float]

    :param freqShearRange: End of inititial guess range. default: `[452.6, 457.6]` Hz
    :type freqShearRange: list[float]

    :param delay: Delay between setting the new frequency and measuring the amplitude. default: `0.75` s
    :type delay: float

    :param denseHalfwidth: Width of densesweep from resonance frequency. default: `3.0` Hz
    :type denseHalfwidth: float

    :param denseStep: Frequency step size used in dense sweep. default: `0.1` Hz
    :type denseStep: float

    :param fitMaxFev: Maximum Fev value for scipy fit. default: `5000`
    :type fitMaxFev: float

    :param accelerometerGConversion: Conversionvalue for accelerometer voltage to g. default: `0.66` V/g
    :type accelerometerGConversion: float

    :param points: How many points to use in coarse sweep as [Normal, Shear]. default: `[7, 7]`
    :type points: list[int]

    :param tolerance: What phase angle is ''good enough''. default: `0.1/180 * \u03c0` RAD
    :type tolerance: float

    :param iterations: Maximum iterations the PLL tries to converge. default: `5`
    :type iterations: int

    :param Kp: Kp value for PLL loop. default: `4 / \u03c0'
    :type Kp: float

    :param debugPrints: How much should be printed to console `['all', 'results', 'none']`, default: 'results'
    :type debugPrints: str

    :returns: [[fResNormal, CNormal, γNormal],[fResShear, CShear, γShear]]
    :rtype: tuple[list[float], list[float]]
    """
    debugPrints: str = kwargs.get("debugPrints", "results")
    g = 9.81

    optNormal, optShear = PLL.PLL2x1D(
        ctrlNormal,
        ctrlShear,
        freqGen,
        freqNormalRange,
        freqShearRange,
        delay=delay,
        points=kwargs.get("points", [7, 7]),
        tolerance=kwargs.get("tolerance", (0.1 / 180) * np.pi),
        iterations=kwargs.get("iterations", 5),
        Kp=kwargs.get("Kp", 4 / np.pi),
        debugPrint=True if debugPrints.lower() in ["all"] else False,
    )

    fNormal = optNormal[0]
    fShear = optShear[0]

    numPts = int(round((2 * denseHalfwidth) / denseStep)) + 1
    freqsDenseNormal = np.linspace(
        fNormal - denseHalfwidth, fNormal + denseHalfwidth, numPts
    )
    ampsDenseNormal = np.empty_like(freqsDenseNormal)
    phasesDenseNormal = np.empty_like(freqsDenseNormal)

    freqsDenseShear = np.linspace(
        fShear - denseHalfwidth, fShear + denseHalfwidth, numPts
    )
    ampsDenseShear = np.empty_like(freqsDenseShear)
    phasesDenseShear = np.empty_like(freqsDenseShear)

    for i, f in enumerate(freqsDenseNormal):
        freqGen.set_frequency(1, f)
        time.sleep(delay)
        ampsDenseNormal[i] = ctrlNormal.readAmplitude()
        phasesDenseNormal[i] = ctrlNormal.readPhase()
        if debugPrints.lower() in ["all"]:
            print(
                f"[CAL] Dense sweep: f={f:.3f} Hz, A={ampsDenseNormal[i]:.6f}, φ={phasesDenseNormal[i]:.2f}"
            )

    for i, f in enumerate(freqsDenseShear):
        freqGen.set_frequency(2, f)
        time.sleep(delay)
        ampsDenseShear[i] = ctrlShear.readAmplitude()
        phasesDenseShear[i] = ctrlShear.readPhase()
        if debugPrints.lower() in ["all"]:
            print(
                f"[CAL] Dense sweep: f={f:.3f} Hz, A={ampsDenseShear[i]:.6f}, φ={phasesDenseShear[i]:.2f}"
            )

    # fit Lorentzian
    ampsDenseNormalMeters = (ampsDenseNormal * accelerometerGConversion) * g
    ω0Normal = 2 * np.pi * fNormal
    C0Normal = np.nanmax(ampsDenseNormalMeters) * ω0Normal
    gamma0Normal = ω0Normal / 10.0

    ampsDenseShearMeters = (ampsDenseShear * accelerometerGConversion) * g
    ω0Shear = 2 * np.pi * fShear
    C0Shear = np.nanmax(ampsDenseShearMeters) * ω0Shear
    gamma0Shear = ω0Shear / 10.0

    def A_model(f, C, gamma_sys, omega0):
        ω = 2 * np.pi * f
        return C / np.sqrt((omega0**2 - ω**2) ** 2 + (gamma_sys * ω) ** 2)

    poptNormal, _ = curve_fit(
        A_model,
        freqsDenseNormal,
        ampsDenseNormalMeters,
        p0=[C0Normal, gamma0Normal, ω0Normal],
        bounds=([0, 0, 0], [np.inf, np.inf, np.inf]),
        nan_policy="omit",
        maxfev=fitMaxFev,
    )
    CNormal, gammaNormal, omega0Normal = poptNormal
    f0Normal = omega0Normal / (2 * np.pi)
    if debugPrints.lower() in ["all", "results"]:
        print(
            f"[CAL] (Normal) Fit results: f_res={f0Normal:.6f} Hz, C={CNormal:.3e}, γ_sys={gammaNormal:.3e}"
        )

    ctrlNormal.setFrequency(round(f0Normal, 6))

    poptShear, _ = curve_fit(
        A_model,
        freqsDenseShear,
        ampsDenseShearMeters,
        p0=[C0Shear, gamma0Shear, ω0Shear],
        bounds=([0, 0, 0], [np.inf, np.inf, np.inf]),
        nan_policy="omit",
        maxfev=fitMaxFev,
    )
    CShear, gammaShear, omega0Shear = poptShear
    f0Shear = omega0Shear / (2 * np.pi)
    if debugPrints.lower() in ["all", "results"]:
        print(
            f"[CAL] (Shear) Fit results: f_res={f0Shear:.6f} Hz, C={CShear:.3e}, γ_sys={gammaShear:.3e}"
        )

    ctrlShear.setFrequency(round(f0Shear, 6))

    return ([f0Normal, CNormal, gammaNormal], [f0Shear, CShear, gammaShear])


def calibrateDistance(
    ctrlNormal: sfa,
    z_stage: pi_e_625,
    height_dev: mitutoyo,
    start_V=10.0,
    max_V=110.0,
    step_V=1.0,
    amp_fraction=0.05,
    delay=0.5,
    **kwargs,
):
    """

    :param debugPrint: If results should constantly be printed, default: False
    :type debugPrint: bool

    Make sure to put the normal mode on resonance with a fitting amplitude.
    """
    debugPrint = kwargs.get("debugPrint", False)

    if debugPrint:
        print(f"\n[DIST] Moving Z-stage to {start_V} V for probe touch...")
    z_stage.absolute_voltage(start_V)
    time.sleep(1)

    input("Adjust probe to surface and back off, then press Enter.")

    A0 = ctrlNormal.readAmplitude()

    if debugPrint:
        print(f"[DIST] Baseline A0 = {A0:.6f}")

    threshold = amp_fraction * A0
    maxPoints = int((max_V - start_V) / step_V) + 1
    amplitudes, heights = maxPoints * [0.0], maxPoints * [0.0]
    voltages = np.linspace(start_V, max_V, maxPoints, endpoint=True)

    for i, voltage in enumerate(voltages):
        z_stage.absolute_voltage(voltage)
        time.sleep(delay)

        A = ctrlNormal.readAmplitude()
        h = height_dev.measurement()

        if debugPrint:
            print(f"[DIST] Approach V={voltage:.1f} → A={A:.6f}, h={h:.3f}")

        amplitudes[i] = A
        heights[i] = h

        if np.isfinite(A) and A < threshold:
            if debugPrint:
                print(
                    f"[DIST] Threshold reached at V={voltage:.1f} V; contact established."
                )

            voltages = voltages[: i + 1]
            amplitudes = amplitudes[: i + 1]
            heights = heights[: i + 1]
            break

    input("Zero the height gauge at contact point, then press Enter.")

    if debugPrint:
        print("[DIST] Retracting from contact back to start...")
    amplitudesRetract, heightsRetract = len(voltages) * [0.0], len(voltages) * [0.0]
    voltagesRetract = np.flip(
        np.linspace(start_V, voltages[-1], len(voltages), endpoint=True)
    )

    for i, voltage in enumerate(voltagesRetract):
        z_stage.absolute_voltage(voltage)
        time.sleep(delay)
        A = ctrlNormal.readAmplitude()
        h = height_dev.measurement()
        if debugPrint:
            print(f"[DIST] Retract V={voltage:.1f} → A={A:.6f}, h={h:.3f}")
        amplitudesRetract[i] = A
        heightsRetract[i] = h

    voltages = np.concatenate((voltages, voltagesRetract))
    amplitudes = np.concatenate((amplitudes, amplitudesRetract))
    heights = np.concatenate((heights, heightsRetract))

    df = pd.DataFrame(
        {"z_voltage": voltages, "amplitude": amplitudes, "height_mm": heights}
    )

    return df


def calibrateC0AmplitudeSingle(
    ctrl: sfa,
    freqGen: RigolDG,
    freqGenChannel: int,
    freqMin: float = 789.5,
    freqMax: float = 794.5,
    delay: float = 0.75,
    denseHalfwidth: float = 3.0,
    denseStep: float = 0.1,
    fitMaxFev: float = 5000,
    accelerometerGConversion: float = 0.66,
    **kwargs,
) -> list[list[float]]:
    """
    Gerates values for C0 and damping factor of the system.

    Requires constant input of new masses until 'done' is typed.

    :param ctrl: Lock-In Amplifier controller.
    :type ctrl: sfa

    :param freqGen: Frequency Generator to use.
    :type freqGen: RigolDG

    :param freqGenChannel: Channel on frequency generator to use.
    :type freqGenChannel: int

    :param freqMin: Start of initial guess range. default: `789.5` Hz
    :type freqMin: float

    :param freqMax: End of inititial guess range. default: `794.5` Hz
    :type freqMax: float

    :param delay: Delay between setting the new frequency and measuring the amplitude. default: `0.75` s
    :type delay: float

    :param denseHalfwidth: Width of densesweep from resonance frequency. default: `3.0` Hz
    :type denseHalfwidth: float

    :param denseStep: Frequency step size used in dense sweep. default: `0.1` Hz
    :type denseStep: float

    :param fitMaxFev: Maximum Fev value for scipy fit. default: `5000`
    :type fitMaxFev: float

    :param accelerometerGConversion: Conversionvalue for accelerometer voltage to g. default: `0.66` V/g
    :type accelerometerGConversion: float

    :param points: How many points to use in coarse sweep. default: `7`
    :type points: int

    :param tolerance: What phase angle is ''good enough''. default: `0.1/180 * \u03c0` RAD
    :type tolerance: float

    :param iterations: Maximum iterations the PLL tries to converge. default: `5`
    :type iterations: int

    :param Kp: Kp value for PLL loop. default: `4 / \u03c0'
    :type Kp: float

    :param debugPrints: How much should be printed to console `['all', 'results', 'none']`, default: 'results'
    :type debugPrints: str

    :returns: list of lists with floats ordered as: \\[Mass (g), Resonance Frequency (Hz), C0 (s\u00b2), Damping system (s\u207b\u00b9)]
    :rtype: list[list[float]]
    """

    results = []

    while True:
        que = input("Input mass (g) or type 'done' when finished: ")
        if que.lower() in ["'done'", "done", "finish", "escape", "cancel", "c"]:
            return results
        try:
            num = float((que.strip().replace(",", ".")).replace("_", ""))
            fRes, C0, gamma = calibrateAirSingle(
                ctrl,
                freqGen,
                freqGenChannel,
                freqMin,
                freqMax,
                delay,
                denseHalfwidth,
                denseStep,
                fitMaxFev,
                accelerometerGConversion,
                **kwargs,
            )
            results += [[num, fRes, C0, gamma]]
        except ValueError:
            print(f"'{que}' is not a valid number!\n")
