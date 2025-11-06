import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt
import os

from newsfa import sfa
from pi_e_625 import pi_e_625
from mitutoyo import mitutoyo
from rigol_dg1022 import RigolDG
from PLL import PLL1D, PLL2D, PLL2x1D
from frequencySweep2D import folderAvailable
from plots import linePlot


def viscosity1D(
    ctrl: sfa,
    freqGen: RigolDG,
    zStage: pi_e_625,
    height_dev: mitutoyo,
    fRes0: float,
    start_V=10.0,
    end_V=110.0,
    step_V=1.0,
    pll_tol=0.1,
    pll_maxiter=25,
    Kp=1 / (4 * np.pi),
    pll_delay=1.5,
    min_amp=0.0003,
):
    current_f = fRes0

    # APPROACH SWEEP
    z_values = np.arange(start_V, end_V + step_V, step_V)
    contact_idx = None

    rows = len(z_values) * [{}]

    for idx, zV in enumerate(z_values):
        print(f"\n[MEAS] Approach Z={zV:.1f} V")
        zStage.absolute_voltage(zV)
        time.sleep(0.5)
        zV_read = zStage.request_voltage()

        # 1) Always measure height first to detect contact
        h = height_dev.measurement()

        if np.isfinite(h) and h > 0.0:
            print(f"[MEAS] Contact detected at Z={zV:.1f} V (h={h:.3f} mm)")
            rows[idx] = {
                "z_voltage_cmd": zV,
                "z_voltage_read": zV_read,
                "height_mm": h,
                "f_res(Hz)": current_f,
                "amplitude(V)": np.nan,
                "phase(deg)": np.nan,
            }
            contact_idx = idx
            if contact_idx + 1 <= len(rows):
                rows = rows[: contact_idx + 1]
            break

        # 2) Then measure amplitude and decide if too small
        A = ctrl.readAmplitude()

        if np.isfinite(A) and A < min_amp:
            print(
                f"[MEAS] A={A:.6f} < {min_amp:.3f}; skipping PLL & phase at Z={zV:.1f} V"
            )
            rows[idx] = {
                "z_voltage_cmd": zV,
                "z_voltage_read": zV_read,
                "height_mm": h,
                "f_res(Hz)": current_f,
                "amplitude(V)": A,
                "phase(deg)": np.nan,
            }
            continue

        current_f, _, _ = PLL1D(
            ctrl,
            freqGen,
            current_f - 1,
            current_f + 1,
            tolerance=pll_tol,
            iterations=pll_maxiter,
            Kp=Kp,
            delay=pll_delay,
        )

        P = ctrl.readPhase()

        print(f"[MEAS] h={h:.3f} mm, A={A:.6f}, phase={P:.2f}")
        rows[idx] = {
            "z_voltage_cmd": zV,
            "z_voltage_read": zV_read,
            "height_mm": h,
            "f_res(Hz)": current_f,
            "amplitude(V)": A,
            "phase(deg)": P,
        }

    # RETRACT SWEEP (back to start_V)
    if contact_idx is not None:
        rows2 = len(z_values[: contact_idx + 1][::-1]) * []
        for idx, zV in enumerate(z_values[: contact_idx + 1][::-1]):
            print(f"\n[MEAS] Retract Z={zV:.1f} V")
            zStage.absolute_voltage(zV)
            time.sleep(0.5)
            zV_read = zStage.request_voltage()

            # height first
            h = height_dev.measurement()

            if np.isfinite(h) and h > 0.0:
                print(f"[MEAS] Contact (retract) at Z={zV:.1f} V (h={h:.3f} mm)")
                rows2[idx] = {
                    "z_voltage_cmd": zV,
                    "z_voltage_read": zV_read,
                    "height_mm": h,
                    "f_res(Hz)": current_f,
                    "amplitude(V)": np.nan,
                    "phase(deg)": np.nan,
                }

                break

            # amplitude next
            A = ctrl.readAmplitude()

            if np.isfinite(A) and A < min_amp:
                print(
                    f"[MEAS] A={A:.6f} < {min_amp:.3f}; skipping PLL & phase at Z={zV:.1f} V"
                )
                rows2[idx] = {
                    "z_voltage_cmd": zV,
                    "z_voltage_read": zV_read,
                    "height_mm": h,
                    "f_res(Hz)": current_f,
                    "amplitude(V)": A,
                    "phase(deg)": np.nan,
                }
                continue

            # PLL + full readout
            current_f, _, _ = PLL1D(
                ctrl,
                freqGen,
                current_f - 1,
                current_f + 1,
                tolerance=pll_tol,
                iterations=pll_maxiter,
                Kp=1 / (4 * np.pi),
                delay=pll_delay,
            )

            P = ctrl.readPhase()

            print(f"[MEAS] h={h:.3f} mm, A={A:.6f}, phase={P:.2f}")
            rows2[idx] = {
                "z_voltage_cmd": zV,
                "z_voltage_read": zV_read,
                "height_mm": h,
                "f_res(Hz)": current_f,
                "amplitude(V)": A,
                "phase(deg)": P,
            }

    # finally reset Z-stage home
    zStage.absolute_voltage(start_V)
    print(f"[MEAS] Z-stage reset to {start_V} V")

    rows.append(rows2)

    # save & plot as before…
    dfm = pd.DataFrame(rows)
    ts = time.strftime("%Y%m%d_%H%M%S")
    filename = f"viscosity_with_PLL_{ts}.csv"
    dfm.to_csv(filename, index=False)
    print(f"[MEAS] Saved data to {filename}")

    for col_x, col_y, xlabel, ylabel, title, fn in [
        (
            "height_mm",
            "amplitude(V)",
            "Height (mm)",
            "Amplitude (V)",
            "Amp vs Height",
            "amp_vs_height",
        ),
        (
            "f_res(Hz)",
            "amplitude(V)",
            "Freq (Hz)",
            "Amplitude (V)",
            "Amp vs Freq",
            "amp_vs_freq",
        ),
        (
            "height_mm",
            "f_res(Hz)",
            "Height (mm)",
            "Res Freq (Hz)",
            "Freq vs Height",
            "freq_vs_height",
        ),
    ]:
        plt.figure(figsize=(6, 4))
        plt.plot(dfm[col_x], dfm[col_y], "o-")
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plotfile = f"{fn}_{ts}.png"
        plt.savefig(plotfile, dpi=300)
        plt.close()
        print(f"[MEAS] Saved plot {plotfile}")

    return rows


def frequencyDependence(
    ctrlNorm: sfa,
    ctrlShea: sfa,
    freqGen: RigolDG,
    freqResMin: float,
    freqResMax: float,
    freqsSweep,
    findNorm: bool = True,
    **kwargs,
):
    """
    Finds resonane frequency while sweeping through the other's frequencies.

    Defaults to checking normal resonance on each shear frequency.
    """
    delay = kwargs.pop("delay", 1.0)

    if "filePath" in kwargs:
        filePath: str = kwargs.pop("filePath")
        if not os.path.exists(filePath):
            os.mkdir(filePath)
    else:
        filePath = folderAvailable(
            path=os.path.abspath("./Data"), name=time.strftime("%Y-%m-%d_%H-%M")
        )
        os.mkdir(filePath)

    open(file=os.path.join(filePath, "freqDepen.csv"), mode="x").close()

    if findNorm:
        channelX = 2
        channelY = 1
        title = "Normal Resonance dependance on Shear"
        xLabel = "Shear Frequency (Hz)"
        yLabel = "Normal Resonance Frequency (Hz)"
    else:
        ctrlNorm, ctrlShea = ctrlShea, ctrlNorm
        channelX = 1
        channelY = 2
        title = "Shear Resonance dependance on Normal"
        xLabel = "Normal Frequency (Hz)"
        yLabel = "Shear Resonance Frequency (Hz)"

    resonance = len(freqsSweep) * [0.0]

    file = open(file=os.path.join(filePath, "freqDepen.csv"), mode="a")
    file.write("Time since Epoch (s), Sweep Frequency (Hz),Resonance Frequency (Hz)\n")
    for idx, fre in enumerate(freqsSweep):
        freqGen.set_frequency(channelX, fre)
        time.sleep(delay)
        res, _, _ = PLL1D(
            ctrl=ctrlNorm,
            freqGen=freqGen,
            freqMin=freqResMin,
            freqMax=freqResMax,
            tolerance=kwargs.get("tolerance", 0.001),
            iterations=kwargs.get("iterations", 11),
            freqGenChannel=channelY,
            Kp=kwargs.get("Kp", 1 / np.pi),
            delay=delay,
        )
        resonance[idx] = res
        file.write(f"{time.time()},{fre},{res}\n")
        file.flush()
    file.close()
    linePlot(
        os.path.join(filePath, "freqDepen.png"),
        freqsSweep,
        resonance,
        xLabel=xLabel,
        yLabel=yLabel,
        title=title,
    )
    
    return resonance
