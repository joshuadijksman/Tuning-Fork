##  The available commands are:
##  Sf (x);   | This command sets the normal frequency to x (note that if the frequency controller is engaged this value will be overwritten)
##  Rf;       | This command returns the current normal frequency
##  Sa (x);   | This command sets the normal sine out amplitude to x (note that if the amplitude controller is engaged this value will be overwritten)
##  Ra;       | This command returns the current normal sine out amplitude
##  Rp;       | This command returns the current normal phase

import serial

from serial.tools import list_ports
from serial.tools.list_ports_common import ListPortInfo

from numpy import nan


def find_unique_dev_by_pidvid(pid: int, vid: int) -> ListPortInfo | None:
    """Find port by Vendor ID and Product ID"""
    found_devices = list(
        filter(lambda p: p.pid == pid and p.vid == vid, list_ports.comports())
    )
    return found_devices[0] if len(found_devices) == 1 else None


def find_unique_dev_by_serial_number(sn: str) -> ListPortInfo | None:
    """Find port by Serial Number"""
    found_devices = list(filter(lambda p: p.serial_number == sn, list_ports.comports()))
    return found_devices[0] if len(found_devices) == 1 else None


class sfa:
    def __init__(self, SN: str, readDrops: int = 3) -> None:
        port = str(find_unique_dev_by_serial_number(sn=SN)).split(" ")[0]
        self.ser = serial.Serial(port, baudrate=9600, timeout=20)
        self.readDrops = readDrops

    def _write(self, cmd: str) -> None:
        senddata = cmd + "\n\r"
        self.ser.write(senddata.encode())
        return

    def _write_read(self, cmd: str) -> str:
        for _ in range(self.readDrops):
            self._write(cmd)
            kar = self.ser.read().decode()
            feedback = kar
            while kar != "\r":
                kar = self.ser.read().decode()
                feedback = feedback + kar
            feedback = feedback.strip()

        return feedback

    def setFrequency(self, frequency: float) -> None:
        """
        # **OBSOLETE** use rigol_dg1022

        Set frequency
        """
        command = "FREQ " + str(round(frequency, 6))
        self._write(command)

    def readFrequency(self) -> float:
        """
        Read frequency

        Reads current frequency set or NaN on bad read.
        """
        command = "FREQ?"
        feedback = self._write_read(command)
        try:
            freq = float(feedback)
        except ValueError:
            freq = nan

        return freq

    def setAmplitude(self, volt: float) -> None:
        """
        Set sine out amplitude voltage.
        """
        self.sine_out_amplitude = round(volt, 6)
        command = "SLVL " + str(self.sine_out_amplitude)

        self._write(command)

    def readAmplitude(self) -> float:
        """
        Read amplitude

        Returns amplitude or NaN on bad read.
        """
        rawA = self._write_read("outp? 3")
        try:
            amp = round(float(rawA), 6)
        except ValueError:
            amp = nan
        return amp

    def readPhase(self) -> float:
        """
        Read phase

        Returns current phase or NaN on bad read.
        """
        command = "OUTP? 4"
        feedback = self._write_read(command)

        try:
            pha = float(feedback)
        except ValueError:
            pha = nan

        return pha
    
    def readSensitivity(self):
        command = "SENS?"
        return self._write_read(command)

    def setSensitivity(self, index: int) -> None:
        """
        Sets lock in amplifiers sensitivity

        Boosts Amplitude if too low.

        | index | sensitivity    |
        |-------|----------------|
        | 0     | 2 nV/fA        |
        | 1     | 5 nV/fA        |
        | 2     | 10 nV/fA       |
        | 3     | 20 nV/fA       |
        | 4     | 50 nV/fA       |
        | 5     | 100 nV/fA      |
        | 6     | 200 nV/fA      |
        | 7     | 500 nV/fA      |
        | 8     | 1 \u00b5V/fA   |
        | 9     | 2 \u00b5V/fA   |
        | 10    | 5 \u00b5V/fA   |
        | 11    | 10 \u00b5V/fA  |
        | 12    | 20 \u00b5V/fA  |
        | 13    | 50 \u00b5V/fA  |
        | 14    | 100 \u00b5V/fA |
        | 15    | 200 \u00b5V/fA |
        | 16    | 500 \u00b5V/fA |
        | 17    | 1 mV/nA        |
        | 18    | 2 mV/nA        |
        | 19    | 5 mV/nA        |
        | 20    | 10 mV/nA       |
        | 21    | 20 mV/nA       |
        | 22    | 50 mV/nA       |
        | 23    | 100 mV/nA      |
        | 24    | 200 mV/nA      |
        | 25    | 500 mV/nA      |
        | 26    | 1 V/\u00b5A    |

        """
        if index < 0:
            raise IndexError(f"Index {index} is too low! (Min 0)")
        elif index > 26:
            raise IndexError(f"Index {index} is too high! (Max 26)")
        command = f"SENS {index}"
        self._write(command)

    def readTimeConstant(self):
        command = "OFLT?"
        return self._write_read(command)

    def setTimeConstant(self, index: int) -> None:
        """
        Sets the time constant

        Time constant sets the duration that the Lock-In Amplifier watches the wave. Make sure `time constant > 1/freq`.

        | index | time constant |
        |-------|---------------|
        | 0     | 10 \u00b5s    |
        | 1     | 30 \u00b5s    |
        | 2     | 100 \u00b5s   |
        | 3     | 300 \u00b5s   |
        | 4     | 1 ms          |
        | 5     | 3 ms          |
        | 6     | 10 ms         |
        | 7     | 30 ms         |
        | 8     | 100 ms        |
        | 9     | 300 ms        |
        | 10    | 1 s           |
        | 11    | 3 s           |
        | 12    | 10 s          |
        | 13    | 30 s          |
        | 14    | 100 s         |
        | 15    | 300 s         |
        | 16    | 1 ks          |
        | 17    | 3 ks          |
        | 18    | 10 ks         |
        | 19    | 30 ks         |
        """
        if index < 0:
            raise IndexError(f"Index {index} is too low! (Min 0)")
        elif index > 19:
            raise IndexError(f"Index {index} is too high! (Max 19)")
        table = [10e-6, 30e-6, 100e-6, 300e-6, 1e-3, 3e-3, 10e-3, 30e-3, 100e-3, 300e-3, 1e0, 3e0, 10e0, 30e0, 100e0, 300e0, 1e3, 3e3, 10e3, 30e3]
        freq = self.readFrequency()
        if table[index]/freq > 1:
            command = f"OFLT {index}"
            self._write(command)
        else:
            raise ValueError(f"Frequency of '{freq}' is too low for time constant '{table[index]}'!")

    def close(self) -> None:
        self.ser.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
