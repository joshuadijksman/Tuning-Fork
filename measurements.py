"""
Independent measurement functions
"""

import os
import time
from datetime import timedelta
import numpy as np

from LockIn_Amplifier import SR830
from Piezo_Controller import E625
from Height_Gauge import mitutoyo
from rigol_dg1022 import RigolDG
from PLL import PLL1D, PLL2D, PLL2x1D
from plots import linePlot, heatmapPlot
from typing import overload


def __folderAvailable(path: os.PathLike, name: str, n=0) -> str:
    """
    Checks if folder is available, returns filepath.

    If folder name is already used, adds ```_n``` to the end, with ```n``` increasing per folder with the same name.
    """
    if n == 0:
        if os.path.exists(os.path.join(path, name)):
            return __folderAvailable(path, name, n=n + 1)
        else:
            if not os.path.exists(path):
                os.mkdir(path)
            return os.path.join(path, name)
    else:
        if os.path.exists(os.path.join(path, name + f"_{n}")):
            return __folderAvailable(path, name, n=n + 1)
        else:
            return os.path.join(path, name + f"_{n}")


@overload
def viscosity1D(
    ctrl: SR830,
    freqGen: RigolDG,
    zStage: E625,
    height_dev: mitutoyo,
    fRes0: float,
): ...
@overload
def viscosity1D(
    ctrl: SR830,
    freqGen: RigolDG,
    zStage: E625,
    height_dev: mitutoyo,
    fRes0: float,
    /,
    start_V: float,
    end_V: float,
    step_V: float,
    pll_tol: float,
    pll_maxiter: int,
    Kp: float,
    pll_delay: float,
    min_amp: float,
    **kwargs,
): ...


def viscosity1D(
    ctrl: SR830,
    freqGen: RigolDG,
    zStage: E625,
    height_dev: mitutoyo,
    fRes0: float,
    start_V=10.0,
    end_V=110.0,
    step_V=1.0,
    pll_tol=0.1,
    pll_maxiter=25,
    Kp=1 / np.pi,
    pll_delay=1.0,
    min_amp=0.0003,
    **kwargs,
):
    if "filePath" in kwargs:
        filePath: str = kwargs.pop("filePath")
        if not os.path.exists(filePath):
            os.mkdir(filePath)
    else:
        filePath = __folderAvailable(
            path=os.path.abspath("./Data"), name=time.strftime("%Y-%m-%d_%H-%M")
        )
        os.mkdir(filePath)

    open(file=os.path.join(filePath, "viscosity1D.csv"), mode="x").close()

    current_f = fRes0

    # APPROACH SWEEP
    z_values = np.arange(start_V, end_V + step_V, step_V)
    contact_idx = None

    rows = len(z_values) * [{}]

    file = open(file=os.path.join(filePath, "viscosity1D.csv"), mode="a")
    file.write(
        "z_voltage_cmd (V),z_voltage_read (V),height (mm),f_res (Hz),amplitude (V),phase (deg)\n"
    )
    file.flush()

    for idx, zV in enumerate(z_values):
        print(f"\n[MEAS] Approach Z={zV:.1f} V")
        zStage.absolute_voltage(zV)
        time.sleep(0.5)
        zV_read = zStage.request_voltage()

        # 1) Always measure height first to detect contact
        h = height_dev.measurement()

        if np.isfinite(h) and h > 0.0:
            print(f"[MEAS] Contact detected at Z={zV:.1f} V (h={h:.3f} mm)")
            file.write(f"{zV},{zV_read},{h},{current_f},{np.nan},{np.nan}\n")
            file.flush()
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
            file.write(f"{zV},{zV_read},{h},{current_f},{A},{np.nan}\n")
            file.flush()
            rows[idx] = {
                "z_voltage_cmd": zV,
                "z_voltage_read": zV_read,
                "height_mm": h,
                "f_res(Hz)": current_f,
                "amplitude(V)": A,
                "phase(deg)": np.nan,
            }
            continue

        current_f, A, P = PLL1D(
            ctrl,
            freqGen,
            current_f - 1,
            current_f + 1,
            tolerance=pll_tol,
            iterations=pll_maxiter,
            Kp=Kp,
            delay=pll_delay,
        )

        print(f"[MEAS] h={h:.3f} mm, A={A:.6f}, phase={P:.2f}")
        file.write(f"{zV},{zV_read},{h},{current_f},{A},{P}\n")
        file.flush()
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
        rows2 = len(z_values[: contact_idx + 1][::-1]) * [{}]
        for idx, zV in enumerate(z_values[: contact_idx + 1][::-1]):
            print(f"\n[MEAS] Retract Z={zV:.1f} V")
            zStage.absolute_voltage(zV)
            time.sleep(0.5)
            zV_read = zStage.request_voltage()

            # height first
            h = height_dev.measurement()

            if np.isfinite(h) and h > 0.0:
                print(f"[MEAS] Contact (retract) at Z={zV:.1f} V (h={h:.3f} mm)")
                file.write(f"{zV},{zV_read},{h},{current_f},{np.nan},{np.nan}\n")
                file.flush()
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
                file.write(f"{zV},{zV_read},{h},{current_f},{A},{np.nan}\n")
                file.flush()
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
            file.write(f"{zV},{zV_read},{h},{current_f},{A},{P}\n")
            file.flush()
            rows2[idx] = {
                "z_voltage_cmd": zV,
                "z_voltage_read": zV_read,
                "height_mm": h,
                "f_res(Hz)": current_f,
                "amplitude(V)": A,
                "phase(deg)": P,
            }
        rows += rows2

    # finally reset Z-stage home
    zStage.absolute_voltage(start_V)
    print(f"[MEAS] Z-stage reset to {start_V} V")

    # save & plot as before…

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
        linePlot(
            fName=os.path.join(filePath, f"{fn}.png"),
            x=[item.get(col_x) for item in rows],
            y=[item.get(col_y) for item in rows],
            xLabel=xlabel,
            yLabel=ylabel,
            title=title,
            dpi=300,
            figsize=(6, 4),
        )
    return rows


def frequencyDependence(
    ctrlNorm: SR830,
    ctrlShea: SR830,
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
        filePath = __folderAvailable(
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


def frequencySweep2D(
    fileName: str | os.PathLike,
    ctrlNormal: SR830,
    ctrlShear: SR830,
    freqGen: RigolDG,
    freqsNormal,
    freqsShear,
    delay: float = 2.0,
    sysDelay: float = 0.777,
) -> None:
    os.makedirs(fileName)

    lenNormal = len(freqsNormal)
    lenShear = len(freqsShear)

    open(file=os.path.join(fileName, "NormalAmp.csv"), mode="x").close()
    open(file=os.path.join(fileName, "ShearAmp.csv"), mode="x").close()
    open(file=os.path.join(fileName, "NormalPha.csv"), mode="x").close()
    open(file=os.path.join(fileName, "ShearPha.csv"), mode="x").close()

    normAmpFile = open(file=os.path.join(fileName, "NormalAmp.csv"), mode="a")
    sheaAmpFile = open(file=os.path.join(fileName, "ShearAmp.csv"), mode="a")
    normPhaFile = open(file=os.path.join(fileName, "NormalPha.csv"), mode="a")
    sheaPhaFile = open(file=os.path.join(fileName, "ShearPha.csv"), mode="a")

    print(
        f"\nExpected loop time: {timedelta(seconds=lenNormal * lenShear * (delay + sysDelay))}\n"
    )
    tPre = time.time()
    for i, fNormal in enumerate(freqsNormal):
        print("Normal: " + str(fNormal) + " (Hz)")
        listNormalAmp = lenShear * [0.0]
        listNormalPha = lenShear * [0.0]
        listShearAmp = lenShear * [0.0]
        listShearPha = lenShear * [0.0]

        freqGen.set_frequency(1, fNormal)
        for j, fShear in enumerate(freqsShear):
            freqGen.set_frequency(2, fShear)
            time.sleep(delay)
            listNormalAmp[j] = ctrlNormal.readAmplitude()
            listNormalPha[j] = ctrlNormal.readPhase()
            listShearAmp[j] = ctrlShear.readAmplitude()
            listShearPha[j] = ctrlShear.readPhase()

        normAmpFile.write(str(listNormalAmp)[1:-1] + "\n")
        sheaAmpFile.write(str(listShearAmp)[1:-1] + "\n")
        normPhaFile.write(str(listNormalPha)[1:-1] + "\n")
        sheaPhaFile.write(str(listShearPha)[1:-1] + "\n")
        normAmpFile.flush()
        sheaAmpFile.flush()
        normPhaFile.flush()
        sheaPhaFile.flush()

    print(f"\nFinished after: {timedelta(seconds=time.time() - tPre)}\n")

    normAmpFile.close()
    sheaAmpFile.close()
    normPhaFile.close()
    sheaPhaFile.close()

    normalAmplitudes = np.genfromtxt(
        os.path.join(fileName, "NormalAmp.csv"), delimiter=","
    )
    normalPhases = np.genfromtxt(os.path.join(fileName, "NormalPha.csv"), delimiter=",")
    shearAmplitudes = np.genfromtxt(
        os.path.join(fileName, "ShearAmp.csv"), delimiter=","
    )
    shearPhases = np.genfromtxt(os.path.join(fileName, "ShearPha.csv"), delimiter=",")

    normalisedAbsoluteAmplitudes = np.sqrt(
        (
            (normalAmplitudes / normalAmplitudes.max()) ** 2
            + (shearAmplitudes / shearAmplitudes.max()) ** 2
        )
        / 2
    )
    heatmapPlot(
        os.path.join(fileName, "NormalAmp.png"),
        normalAmplitudes,
        freqsShear,
        freqsNormal,
        title="Normal Amplitudes",
    )
    heatmapPlot(
        os.path.join(fileName, "ShearAmp.png"),
        shearAmplitudes,
        freqsShear,
        freqsNormal,
        title="Shear Amplitudes",
    )
    heatmapPlot(
        os.path.join(fileName, "NormalisedAmp.png"),
        normalisedAbsoluteAmplitudes,
        freqsShear,
        freqsNormal,
        title="Normalised Amplitudes",
    )

    normalisedAbsolutePhases = np.sqrt(
        (
            (normalPhases / normalPhases.max()) ** 2
            + (shearPhases / shearPhases.max()) ** 2
        )
        / 2
    )
    heatmapPlot(
        os.path.join(fileName, "NormalPha.png"),
        normalPhases,
        freqsShear,
        freqsNormal,
        title="Normal Phases",
    )
    heatmapPlot(
        os.path.join(fileName, "ShearPha.png"),
        shearPhases,
        freqsShear,
        freqsNormal,
        title="Shear Phases",
    )
    heatmapPlot(
        os.path.join(fileName, "NormalisedPha.png"),
        normalisedAbsolutePhases,
        freqsShear,
        freqsNormal,
        title="Normalised Phases",
    )

    ctrlNormal.ser.close()
    ctrlShear.ser.close()
