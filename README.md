# Tuning-Fork

## Overview
The Tuning-Fork repository contains code related to the tuning fork setup at UvA. The code in this repository is meant to assist with measurements and control the setup.

## Features
- [To be added] A Graphical User Interface for interaction with the setup.
- Calibration of parameters (See [calibration.py](calibration.py)):
  - Function Constants
  - Effective Mass Calibration
  - Distance Calibration

- Phase Lock Loop for finding the resonance frequency. (See [PLL.py](PLL.py))
- Several measurements (See [measurements.py](measurements.py)):
  - Viscosity (1 & 2 axis)
  - Frequency Dependence between both axis (1 & 2 axis sweep)

- Integration and control of various instruments:
  - [SRS Lock-In Amplifier](https://www.thinksrs.com/products/sr830.html) ([LockIn_Amplifier.py](LockIn_Amplifier.py))
  - [PI E-625 Piezo Servo Controller](https://www.pi-usa.us/en/products/piezo-drivers-controllers-power-supplies-high-voltage-amplifiers/e-625-piezo-servo-controller-driver-604100/) ([Piezo_Controller.py](Piezo_Controller.py))
  - [Mitutoyo](https://shop.mitutoyo.eu) ([Height_Gauge.py](Height_Gauge.py))
  
  Instrument control from dependencies:
  - [RIGOL DG1062z](https://rigol.com.ua/en/products/arbitrary-waveform-function-generator-rigol-dg1062z/) ([rigol-dg1022](https://pypi.org/project/rigol-dg1022/))

## GUI
The GUI is not finished and lacks most support. See the [`GUI` branch](https://github.com/joshuadijksman/Tuning-Fork/tree/GUI) for more information and updates.

## Installation
To install the necessary dependencies, run:
```bash
pip install -r requirements.txt
```
Or, preferably, make a new virtual environment that includes the dependencies in [requirements.txt](requirements.txt).