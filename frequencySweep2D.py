import newsfa as sfa
import os
import time
from datetime import timedelta
import numpy as np
from rigol_dg1022 import RigolDG
from plots import heatmapPlot


def folderAvailable(path, name, n=0) -> str:
    """
    Checks if folder is available, returns filepath.

    If folder name is already used, adds ```_n``` to the end, with ```n``` increasing per folder with the same name.
    """
    if n == 0:
        if os.path.exists(os.path.join(path, name)):
            return folderAvailable(path, name, n=n+1)
        else:
            return os.path.join(path, name)
    else:
        if os.path.exists(os.path.join(path, name + f"_{n}")):
            return folderAvailable(path, name, n=n+1)
        else:
            return os.path.join(path, name+f"_{n}")


def frequencySweep2D(
    fileName: str,
    ctrlNormal: sfa.sfa,
    ctrlShear: sfa.sfa,
    freqGen: RigolDG,
    freqsNormal,
    freqsShear,
    delay: float = 2.,
    sysDelay: float = 0.777
    ) -> None:

    os.makedirs(fileName)

    lenNormal = len(freqsNormal)
    lenShear = len(freqsShear)

    open(file=os.path.join(fileName,"NormalAmp.csv"), mode="x").close()
    open(file=os.path.join(fileName,"ShearAmp.csv") , mode="x").close()
    open(file=os.path.join(fileName,"NormalPha.csv"), mode="x").close()
    open(file=os.path.join(fileName,"ShearPha.csv") , mode="x").close()

    normAmpFile = open(file=os.path.join(fileName,"NormalAmp.csv"), mode="a")
    sheaAmpFile = open(file=os.path.join(fileName,"ShearAmp.csv"), mode="a")
    normPhaFile = open(file=os.path.join(fileName,"NormalPha.csv"), mode="a")
    sheaPhaFile = open(file=os.path.join(fileName,"ShearPha.csv"), mode="a")
    

    print(f"\nExpected loop time: {timedelta(seconds=lenNormal*lenShear*(delay+sysDelay))}\n")
    tPre = time.time()
    for i, fNormal in enumerate(freqsNormal):
        print("Normal: "+str(fNormal)+" (Hz)")
        listNormalAmp = lenShear*[0.]
        listNormalPha = lenShear*[0.]
        listShearAmp = lenShear*[0.]
        listShearPha =lenShear*[0.]

        freqGen.set_frequency(1, fNormal)
        for j, fShear in enumerate(freqsShear):
            freqGen.set_frequency(2, fShear)
            time.sleep(delay)
            try:
                listNormalAmp[j] = ctrlNormal.readAmplitude()
            except:
                listNormalAmp[j] = np.nan

            try:
                listNormalPha[j] = ctrlNormal.readPhase()
            except:
                listNormalPha[j] = np.nan

            try:
                listShearAmp[j] = ctrlShear.readAmplitude()
            except:
                listShearAmp[j] = np.nan

            try:
                listShearPha[j] = ctrlShear.readPhase()
            except:
                listShearPha[j] = np.nan

        normAmpFile.write(str(listNormalAmp)[1:-1]+"\n")
        sheaAmpFile.write(str(listShearAmp)[1:-1]+"\n")
        normPhaFile.write(str(listNormalPha)[1:-1]+"\n")
        sheaPhaFile.write(str(listShearPha)[1:-1]+"\n")
        normAmpFile.flush()
        sheaAmpFile.flush()
        normPhaFile.flush()
        sheaPhaFile.flush()

    print(f"\nFinished after: {timedelta(seconds=time.time()-tPre)}\n")

    normAmpFile.close()
    sheaAmpFile.close()
    normPhaFile.close()
    sheaPhaFile.close()

    normalAmplitudes= np.genfromtxt(os.path.join(fileName,"NormalAmp.csv"), delimiter=",")
    normalPhases    = np.genfromtxt(os.path.join(fileName,"NormalPha.csv") , delimiter=",")
    shearAmplitudes = np.genfromtxt(os.path.join(fileName,"ShearAmp.csv"), delimiter=",")
    shearPhases     = np.genfromtxt(os.path.join(fileName,"ShearPha.csv") , delimiter=",")

    normalisedAbsoluteAmplitudes = np.sqrt(((normalAmplitudes/normalAmplitudes.max())**2+(shearAmplitudes/shearAmplitudes.max())**2)/2)
    heatmapPlot(os.path.join(fileName,"NormalAmp.png"), normalAmplitudes, freqsShear, freqsNormal, title="Normal Amplitudes")
    heatmapPlot(os.path.join(fileName,"ShearAmp.png") , shearAmplitudes, freqsShear, freqsNormal, title="Shear Amplitudes")
    heatmapPlot(os.path.join(fileName,"NormalisedAmp.png"), normalisedAbsoluteAmplitudes, freqsShear, freqsNormal, title="Normalised Amplitudes")
    
    normalisedAbsolutePhases= np.sqrt(((normalPhases/normalPhases.max())**2+(shearPhases/shearPhases.max())**2)/2)
    heatmapPlot(os.path.join(fileName,"NormalPha.png"),     normalPhases, freqsShear, freqsNormal, title="Normal Phases")
    heatmapPlot(os.path.join(fileName,"ShearPha.png") ,      shearPhases, freqsShear, freqsNormal, title="Shear Phases")
    heatmapPlot(os.path.join(fileName,"NormalisedPha.png"), normalisedAbsolutePhases, freqsShear, freqsNormal, title="Normalised Phases")

    ctrlNormal.ser.close()
    ctrlShear.ser.close()


if __name__ == "__main__":
    resolution = 1

    freqNormalStart=789.5
    freqNormalEnd=794.5

    freqShearStart=452.6
    freqShearEnd=457.6

    freqsNormal = np.linspace(freqNormalStart, freqNormalEnd, int((freqNormalEnd-freqNormalStart)/resolution+1), endpoint=True)
    freqsShear = np.linspace(freqShearStart, freqShearEnd, int((freqShearEnd-freqShearStart)/resolution+1), endpoint=True)

    ctrlNormal: sfa.sfa = sfa.sfa(SN="A9JSTXTQA")
    ctrlShear: sfa.sfa = sfa.sfa(SN="A9TQAG5OA")

    freqGen = RigolDG()
    freqGen.set_waveform(1, "SIN")
    freqGen.set_waveform(2, "SIN")
    freqGen.set_output(1, True)
    freqGen.set_output(2, True)

    fileName = folderAvailable(
        path = os.path.abspath("./Data"),
        name = time.strftime("%Y-%m-%d_%H-%M")
    )

    frequencySweep2D(
        fileName,
        freqGen=freqGen,
        ctrlNormal=ctrlNormal,
        ctrlShear=ctrlShear,
        freqsNormal=freqsNormal,
        freqsShear=freqsShear,
        delay = 0.5
    )