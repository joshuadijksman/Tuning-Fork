import numpy as np
from rigol_dg1022 import RigolDG

from Piezo_Controller import E625
from Height_Gauge import mitutoyo
from measurements import frequencyDependence
from LockIn_Amplifier import SR830


def main() -> None:
    ctrlNormal: SR830 = SR830(SN="A9JSTXTQA")
    ctrlShear: SR830 = SR830(SN="A9TQAG5OA")
    freqGen: RigolDG = RigolDG()
    zStage = E625()
    hDev = mitutoyo()

    freqGen.set_waveform(1, "SIN")
    freqGen.set_waveform(2, "SIN")
    freqGen.set_output(1, True)
    freqGen.set_output(2, True)

    # optNormal, optShear = calibrateAir(ctrlNormal, ctrlShear)
    # calibrateDistance(ctrlNormal, zStage, hDev)

    findNorm = True

    fNormalMin = 790
    fNormalMax = 810

    fShearMin = 400
    fShearMax = 500

    resolution = 0.01

    if findNorm:
        freqs = np.linspace(
            fShearMin,
            fShearMax,
            int((fShearMax - fShearMin) / resolution + 1),
            endpoint=True,
        )
        frequencyDependence(
            ctrlNormal,
            ctrlShear,
            freqGen,
            790,
            810,
            freqs,
        )
    else:
        freqs = np.linspace(
            fNormalMin,
            fNormalMax,
            int((fNormalMax - fNormalMin) / resolution + 1),
            endpoint=True,
        )
        frequencyDependence(
            ctrlNormal, ctrlShear, freqGen, fShearMin, fShearMax, freqs, findNorm=False
        )
    
    freqGen.set_output(1, False)
    freqGen.set_output(2, False)
    freqGen.close()

    ctrlNormal.close()
    ctrlShear.close()

    hDev.close()
    zStage.close()
    

if __name__ == "__main__":
    main()
