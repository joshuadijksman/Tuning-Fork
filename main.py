import numpy as np
from rigol_dg1022 import RigolDG

from pi_e_625 import pi_e_625
from mitutoyo import mitutoyo
from measurements import frequencyDependence
from newsfa import sfa


def main() -> None:
    ctrlNormal: sfa = sfa(SN="A9JSTXTQA")
    ctrlShear: sfa = sfa(SN="A9TQAG5OA")
    freqGen: RigolDG = RigolDG()
    zStage = pi_e_625()
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
