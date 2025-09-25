import numpy as np
from scipy.optimize import curve_fit
import time
import matplotlib.pyplot as plt
import pandas as pd

from newsfa import sfa
import PLL
from pi_e_625 import pi_e_625
from mitutoyo import mitutoyo


def calibrateAir(  
        ctrlNormal: sfa,
        ctrlShear: sfa,
        freqNormalRange: list[int | float] = [789.5, 794.5],
        freqShearRange: list[int | float] = [452.6, 457.6],
        delay: int | float = 0.75,
        sampleDrops: int = 3,
        denseHalfwidth = 3.0,
        denseStep = 0.1,
        fitMaxFev=5000
        ) -> tuple[list[int|float], list[int|float]]:

    optNormal, optShear = PLL.PLL2x1D(
        ctrlNormal,
        ctrlShear,
        freqNormalRange,
        freqShearRange,
        delay,
        sampleDrops=sampleDrops,
        points=[7, 7]
    )

    fNormal = optNormal[0]
    fShear = optShear[0]

    numPts = int(round((2*denseHalfwidth) / denseStep)) + 1
    freqsDenseNormal = np.linspace(fNormal - denseHalfwidth, fNormal + denseHalfwidth, numPts)
    ampsDenseNormal = np.empty_like(freqsDenseNormal)
    phasesDenseNormal = np.empty_like(freqsDenseNormal)

    freqsDenseShear = np.linspace(fShear - denseHalfwidth, fShear + denseHalfwidth, numPts)
    ampsDenseShear = np.empty_like(freqsDenseShear)
    phasesDenseShear = np.empty_like(freqsDenseShear)

    for i, f in enumerate(freqsDenseNormal):
        ctrlNormal.Sf(f)
        time.sleep(delay)
        try:
            ampsDenseNormal[i] = ctrlNormal.Rm()
        except:
            ampsDenseNormal[i] = np.nan
        try:
            phasesDenseNormal[i] = ctrlNormal.Rp()
        except:
            phasesDenseNormal[i] = np.nan
        print(f"[CAL] Dense sweep: f={f:.3f} Hz, A={ampsDenseNormal[i]:.6f}, φ={phasesDenseNormal[i]:.2f}")

    for i, f in enumerate(freqsDenseShear):
        ctrlShear.Sf(f)
        time.sleep(delay)
        try:
            ampsDenseShear[i] = ctrlShear.Rm()
        except:
            ampsDenseShear[i] = np.nan
        try:
            phasesDenseShear[i] = ctrlShear.Rp()
        except:
            phasesDenseShear[i] = np.nan
        print(f"[CAL] Dense sweep: f={f:.3f} Hz, A={ampsDenseShear[i]:.6f}, φ={phasesDenseShear[i]:.2f}")
    

    # fit Lorentzian
    ω0Normal = 2*np.pi*fNormal
    C0Normal = np.nanmax(ampsDenseNormal)*ω0Normal
    gamma0Normal = ω0Normal/10.0

    ω0Shear = 2*np.pi*fShear
    C0Shear = np.nanmax(ampsDenseShear)*ω0Shear
    gamma0Shear = ω0Shear/10.0

    def A_model(f, C, gamma_sys, omega0):
        ω = 2*np.pi*f
        return C/np.sqrt((omega0**2-ω**2)**2 + (gamma_sys*ω)**2)
    
    poptNormal, _ = curve_fit(
        A_model,
        freqsDenseNormal,
        ampsDenseNormal,
        p0=[C0Normal, gamma0Normal, ω0Normal],
        bounds=([0,0,0],[np.inf,np.inf,np.inf]),
        nan_policy="omit",
        maxfev=fitMaxFev
    )
    CNormal, gammaNormal, omega0Normal = poptNormal
    f0Normal = omega0Normal/(2*np.pi)
    print(f"[CAL] (Normal) Fit results: C={CNormal:.3e}, γ_sys={gammaNormal:.3e}, f_res={f0Normal:.6f} Hz")

    ctrlNormal.Sf(round(f0Normal,6))

    poptShear, _ = curve_fit(
        A_model,
        freqsDenseShear,
        ampsDenseShear,
        p0=[C0Shear, gamma0Shear, ω0Shear],
        bounds=([0,0,0],[np.inf,np.inf,np.inf]),
        nan_policy="omit",
        maxfev=fitMaxFev
    )
    CShear, gammaShear, omega0Shear = poptShear
    f0Shear = omega0Shear/(2*np.pi)
    print(f"[CAL] (Shear) Fit results: C={CShear:.3e}, γ_sys={gammaShear:.3e}, f_res={f0Shear:.6f} Hz")

    ctrlShear.Sf(round(f0Shear,6))

    return [f0Normal, CNormal, gammaNormal], [f0Shear, CShear, gammaShear]

def calibrateDistance(ctrlNormal: sfa, 
                       z_stage: pi_e_625, 
                       height_dev: mitutoyo,
                       start_V=10.0, 
                       max_V=110.0, 
                       step_V=1.0,
                       amp_fraction=0.05,
                       delay = 0.5
                       ):
    """
    

    Make sure to put the normal mode on resonance with a fitting amplitude.
    """

    print(f"\n[DIST] Moving Z-stage to {start_V} V for probe touch...")
    z_stage.absolute_voltage(start_V)
    time.sleep(1)
    input("Adjust probe to surface and back off, then press Enter.")

    A0 = ctrlNormal.Rm()

    print(f"[DIST] Baseline A0 = {A0:.6f}")

    threshold = amp_fraction * A0
    maxPoints = int((max_V-start_V)/step_V)+1
    amplitudes, heights = maxPoints*[0.], maxPoints*[0.]
    voltages = np.linspace(start_V, max_V, maxPoints, endpoint=True)
    
    for i, voltage in enumerate(voltages):
        z_stage.absolute_voltage(voltage)
        time.sleep(delay)

        try:
            A = ctrlNormal.Rm()
        except:
            A = np.nan
        try:
            h = height_dev.measurement()
        except:
            h = np.nan

        print(f"[DIST] Approach V={voltage:.1f} → A={A:.6f}, h={h:.3f}")

        amplitudes[i]=A
        heights[i]=h

        if np.isfinite(A) and A < threshold:
            print(f"[DIST] Threshold reached at V={voltage:.1f} V; contact established.")

            voltages = voltages[:i+1]
            amplitudes = amplitudes[:i+1]
            heights = heights[:i+1]
            break

    input("Zero the height gauge at contact point, then press Enter.")

    print("[DIST] Retracting from contact back to start...")
    amplitudesRetract, heightsRetract = len(voltages)*[0.], len(voltages)*[0.]
    voltagesRetract = np.flip(np.linspace(start_V, voltages[-1], len(voltages), endpoint=True))

    for i, voltage in enumerate(voltagesRetract):
        z_stage.absolute_voltage(voltage)
        time.sleep(delay)
        try:
            A = ctrlNormal.Rm()
        except:
            A = np.nan
        try:
            h = height_dev.measurement()
        except:
            h = np.nan
        print(f"[DIST] Retract V={voltage:.1f} → A={A:.6f}, h={h:.3f}")
        amplitudesRetract[i] = A
        heightsRetract[i] = h

    voltages = np.concatenate((voltages, voltagesRetract))
    amplitudes = np.concatenate((amplitudes, amplitudesRetract))
    heights = np.concatenate((heights, heightsRetract))

    df = pd.DataFrame({
        "z_voltage": voltages,
        "amplitude": amplitudes,
        "height_mm": heights
    })

    return df


def main() -> None:
    ctrlNormal: sfa = sfa(PID=0x7523, VID=0x1A86)
    ctrlShear: sfa = sfa(PID=0x6001, VID=0x0403)
    zStage = pi_e_625()
    hDev = mitutoyo()

    ctrlNormal.Sa(0.006)
    ctrlShear.Sa(0.012)

    optNormal, optShear = calibrateAir(ctrlNormal, ctrlShear)

    calibrateDistance(ctrlNormal, zStage, hDev)



if __name__ == "__main__":
    main()