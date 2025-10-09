import newsfa as sfa
import os
import time
from datetime import timedelta
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from rigol_dg1022 import RigolDG

def heatmapPlot(fName: str, data: list[list[int|float]] | np.ndarray, xTickLabels: list[int|float] = [], yTickLabels: list[int|float] = [], title: str = "", xTicks: int = 10, yTicks: int = 10, xTickLabelRound: int = 4, yTickLabelRound: int = 4, figsize=(9,6)) -> None:
    fig = plt.figure(None, figsize)
    
    ax = sns.heatmap(data)

    if len(xTickLabels)!=0:
        ax.set_xlabel("Shear Frequency (Hz)")
        if len(xTickLabels)>=xTicks: 
            xStep = int(len(data[0])/xTicks)
            xSpots = list(range(0, len(data[0])+1, xStep))
            ax.set_xticks(ticks=np.array(xSpots)+0.5)
        
            if len(xTickLabels)==xTicks:
                ax.set_xticklabels(xTickLabels) 
            else:
                step = int(len(xTickLabels)/xTicks)
                for i, _ in enumerate(xSpots):
                    xSpots[i] = round(xTickLabels[i*step], xTickLabelRound)
                ax.set_xticklabels(xSpots)
        
    if len(yTickLabels)!=0:
        ax.set_ylabel("Normal Frequency (Hz)")
        if len(yTickLabels)>=yTicks:
            yStep = int(len(data)/yTicks)
            ySpots = list(range(0, len(data)+1, yStep))
            ax.set_yticks(np.array(ySpots)+0.5)

            if len(yTickLabels)==yTicks:
                ax.set_yticklabels(yTickLabels)
            else:
                step = int(len(yTickLabels)/yTicks)
                for i, _ in enumerate(ySpots):
                    ySpots[i] = round(yTickLabels[i*step], yTickLabelRound)
                ax.set_yticklabels(ySpots)
    
    if title != "":
        ax.set_title(title)

    fig.axes.append(ax)
    fig.savefig(fName, bbox_inches="tight")


def fileAvailable(folder, name, n=0) -> str:
    if n == 0:
        if os.path.exists(os.path.join(folder, name)):
            return fileAvailable(folder, name, n=n+1)
        else:
            return os.path.join(folder, name)
    else:
        if os.path.exists(os.path.join(folder, name + f"_{n}")):
            return fileAvailable(folder, name, n=n+1)
        else:
            return os.path.join(folder, name+f"_{n}")


def frequencySweep2D(
    fileName: str,
    ctrlNormal: sfa.sfa,
    ctrlShear: sfa.sfa,
    freqGen: RigolDG,
    freqsNormal,
    freqsShear,
    delay: float = 2.,
    sampleDrops: int = 3,
    sysDelay: float = 0.777
    ) -> None:

    os.makedirs(fileName)

    lenNormal = len(freqsNormal)
    lenShear = len(freqsShear)

    ctrlShear.Sa(0.02)
    ctrlNormal.Sa(0.006)

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
                listNormalAmp[j] = [ctrlNormal.Rm() for _ in range(sampleDrops+1)][-1]
            except:
                listNormalAmp[j] = np.nan

            try:
                listNormalPha[j] = [ctrlNormal.Rp() for _ in range(sampleDrops+1)][-1]
            except:
                listNormalPha[j] = np.nan

            try:
                listShearAmp[j] = [ctrlShear.Rm() for _ in range(sampleDrops+1)][-1]
            except:
                listShearAmp[j] = np.nan

            try:
                listShearPha[j] = [ctrlShear.Rp() for _ in range(sampleDrops+1)][-1]
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

    fileName = fileAvailable(
        folder = os.path.abspath("./Data"),
        name = time.strftime("%Y-%m-%d_%H-%M")
    ).split(".")[0]

    frequencySweep2D(
        fileName,
        freqGen=freqGen,
        ctrlNormal=ctrlNormal,
        ctrlShear=ctrlShear,
        freqsNormal=freqsNormal,
        freqsShear=freqsShear,
        delay = 0.5,
        sampleDrops = 5
    )