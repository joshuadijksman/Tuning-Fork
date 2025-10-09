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

def find_unique_dev_by_pidvid(vid: int, pid: int) -> ListPortInfo | None:
     """Find port by Vendor ID and Product ID"""
     found_devices = list(filter(lambda p:p.vid == vid and p.pid == pid, list_ports.comports())) #  p.pid == pid and p.vid == vid and 
     return found_devices[0] if len(found_devices) == 1 else None


def find_unique_dev_by_serial_number(sn: str) -> ListPortInfo | None:
     """Find port by Serial Number"""
     found_devices = list(filter(lambda p:p.serial_number == sn, list_ports.comports())) #  p.pid == pid and p.vid == vid and 
     return found_devices[0] if len(found_devices) == 1 else None


class sfa():

    def __init__(self, SN: str, readDrops: int = 3) -> None:
        port = str(find_unique_dev_by_serial_number(sn=SN)).split(" ")[0]
        self.ser = serial.Serial(port, baudrate=9600,timeout=20)
        self.readDrops = readDrops
        

    def __write(self, cmd: str) -> None:
        senddata = cmd  + '\n\r'
        self.ser.write(senddata.encode())
        return


    def __write_read(self, cmd: str) -> str:
        self.__write(cmd)

        for _ in range(self.readDrops):
            kar = self.ser.read().decode()
            feedback = kar
            while kar != '\r':
                kar = self.ser.read().decode()
                feedback = feedback + kar
            feedback = feedback.strip()
            
        return feedback


    def setFrequency (self, frequency: float) -> None:
        """
        # **OBSOLETE** use rigol_dg1022
        
        Set frequency
        """
        command = "FREQ " + str(round(frequency,6))
        self.__write(command)


    def readFrequency(self) -> float:
        """
        Read frequency

        Reads current frequency set or NaN on bad read.
        """
        command = "FREQ?"
        feedback = self.__write_read(command)
        try:
            freq = float(feedback)
        except ValueError:
            freq = nan
        
        return freq

    def setAmplitude (self, volt: float) -> None:
        """
        Set normal sine out amplitude voltage.
        """
        self.sine_out_amplitude = round(volt,6)
        command = "SLVL "  + str(self.sine_out_amplitude)
        
        self.__write(command)


    def readAmplitude(self) -> float:
        """
        Read amplitude

        Returns amplite  or NaN on bad read.
        """
        rawA = self.__write_read("outp? 3")
        try:
            amp = round(float(rawA),6)
        except ValueError:
            amp = nan
        return amp
    

    def readPhase (self) -> float:
        """
        Read phase

        Returns current normal phase or NaN on bad read.
        """
        command = "OUTP? 4"
        feedback = self.__write_read(command)

        try:
            pha = float(feedback)
        except ValueError:
            pha = nan

        return pha