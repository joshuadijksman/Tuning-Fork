import serial
from serial.tools import list_ports
from numpy import nan

def port_find_unique_dev_by_pidvid(pid: int, vid: int):
    found_devices = list(filter(lambda p: p.pid == pid and p.vid == vid, list_ports.comports()))
    print("Found Mitutoyo device(s):", found_devices)
    return found_devices[0] if len(found_devices) == 1 else None

class mitutoyo(object):
    def __init__(self, port='') -> None:
        if port == "":
            port = str(port_find_unique_dev_by_pidvid(0x4001, 0x0fe7)).split(" ")[0]
            print("Using Mitutoyo port:", port)
        self.ser = serial.Serial(port=port, baudrate=115200)

    def answer(self) -> str:
        f = self.ser.read().decode()
        a: str = ""
        c: str = ""

        while c != '\r':
            c = self.ser.read().decode()

            if c != '\r':
                a += c

        if f == '9':
            print("Error")

        return a

    def measurement(self) -> float:
        """
        Measures height
        
        Returns height value or nan on bad read.
        """
        m: float = 0.
        cmd = "1\r".encode()
        self.ser.write(cmd)
        a = self.answer().split('\r')[0]

        if a.startswith('1A'):
            try:
                m = float(a.replace('1A', ""))
            except ValueError:
                m = nan
        return m

    def info(self) -> str:
        cmd = "V\r".encode()
        self.ser.write(cmd)
        a = self.answer()

        return a
