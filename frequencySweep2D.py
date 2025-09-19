import newsfa as sfa
import os
import time
from datetime import timedelta
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def heatmapPlot(fName, data, xTickLabels: list | None=None, yTickLabels: list | None=None, title: str = "Amplitude", xTicks=list(range(5)), yTicks=list(range(5))) -> None:
    fig = plt.figure()
    
    ax = sns.heatmap(data)

    # if (not (type(xTickLabels)==None))  and (not (type(yTickLabels)==None)):
    #     ax.set_xticks(xTicks)
    #     if len(xTickLabels)==len(xTicks):
    #         ax.set_xticklabels(xTickLabels)
    #     else:
    #         step = int(len(xTickLabels)/len(xTicks))
    #         z=0
    #         for i, _ in enumerate(xTicks):
    #             xTicks[i] = xTickLabels[z]
    #             z+=step
    #         ax.set_xticklabels(xTicks)
        
    #     ax.set_yticks(yTicks)
    #     if len(yTickLabels)==len(yTicks):
    #         ax.set_yticklabels(yTickLabels)
    #     else:
    #         step = int(len(yTickLabels)/len(yTicks))
    #         z=0
    #         for i, _ in enumerate(yTicks):
    #             yTicks[i] = yTickLabels[z]
    #             z+=step
    #         ax.set_yticklabels(yTicks)

    ax.set_ylabel("Normal Frequency (Hz)")
    ax.set_xlabel("Shear Frequency (Hz)")

    ax.set_title(title)

    fig.axes.append(ax)
    fig.savefig(fName)


def fileAvailable(folder, name, ext = ".csv", n=1) -> str:
    if os.path.exists(os.path.join(folder, name + f"_{n}" + ext)):
        return fileAvailable(folder, name, ext, n+1)
    else:
        return os.path.join(folder, name+f"_{n}" + ext)


def main(
    fileName: str,
    freqsNormal,
    freqsShear,
    delay: float = 2.,
    sampleDrops: int = 3,
    ):

    lenNormal = len(freqsNormal)
    lenShear = len(freqsShear)

    ctrlShear = sfa.sfa()
    ctrlNormal = sfa.sfa(PID=0x6001, VID=0x0403)

    ctrlShear.Sa(0.02)
    ctrlNormal.Sa(0.006)

    normalAmplitudes = np.zeros((lenNormal,lenShear))
    shearAmplitudes = np.zeros((lenNormal,lenShear))    

    print(f"\nExpected loop time: {timedelta(seconds=lenNormal*lenShear*delay)}\n")
    tPre = time.time()

    for i, fNormal in enumerate(freqsNormal):
        print("Normal: "+str(fNormal)+" (Hz)")
        listNormal = np.zeros(lenNormal)
        listShear = np.zeros(lenShear)
        ctrlNormal.Sf(fNormal)
        for j, fShear in enumerate(freqsShear):
            ctrlShear.Sf(fShear)
            time.sleep(delay)
            try:
                listNormal[j] = [ctrlNormal.Rp() for _ in range(sampleDrops+1)][-1]
            except:
                listNormal[j] = np.nan
            try:
                listShear[j] = [ctrlShear.Rp() for _ in range(sampleDrops+1)][-1]
            except:
                listShear[j] = np.nan
        normalAmplitudes[i] = listNormal
        shearAmplitudes[i] = listShear
    
    print(f"\nFinished after: {timedelta(seconds=time.time()-tPre)}\n")
    
    np.savetxt(fileName+"_Normal.csv", normalAmplitudes, delimiter=",")
    np.savetxt(fileName+"_Shear.csv", shearAmplitudes, delimiter=",")

    relativeAbsoluteAmplitudes = np.sqrt(((normalAmplitudes/normalAmplitudes.max())**2+(shearAmplitudes/shearAmplitudes.max())**2)/2)
    heatmapPlot(fileName+"_Normal.png", normalAmplitudes, freqsShear, freqsNormal, title="Normal Amplitudes")
    heatmapPlot(fileName+"_Shear.png", shearAmplitudes, freqsShear, freqsNormal, title="Shear Amplitudes")
    heatmapPlot(fileName+"_Relative.png", relativeAbsoluteAmplitudes, freqsShear, freqsNormal, title="Relative Amplitudes")

    ctrlNormal.ser.close()
    ctrlShear.ser.close()

if __name__ == "__main__":
    resolution = 1

    freqNormalStart=789.5
    freqNormalEnd=794.5

    freqShearStart=452.6
    freqShearEnd=457.6

    freqsNormal = np.linspace(freqNormalStart, freqNormalEnd, int((freqNormalEnd-freqNormalStart+1)/resolution), endpoint=True)
    freqsShear = np.linspace(freqShearStart, freqShearEnd, int((freqShearEnd-freqShearStart+1)/resolution), endpoint=True)

    fileName = fileAvailable(
        folder = os.path.abspath("./Data"),
        name = time.strftime("%Y-%m-%d_%H-%M")
    ).split(".")[0]

    main(
        fileName,
        freqsNormal=freqsNormal,
        freqsShear=freqsShear,
        delay = 1,
        sampleDrops = 5
    )