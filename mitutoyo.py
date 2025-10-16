import serial
from numpy import nan
from newsfa import find_unique_dev_by_pidvid


class mitutoyo(object):
    def __init__(self, port="") -> None:
        if port == "":
            port = str(find_unique_dev_by_pidvid(0x4001, 0x0FE7)).split(" ")[0]
            print("Using Mitutoyo port:", port)
        self.ser = serial.Serial(port=port, baudrate=115200)

    def answer(self) -> str:
        f = self.ser.read().decode()
        a: str = ""
        c: str = ""

        while c != "\r":
            c = self.ser.read().decode()

            if c != "\r":
                a += c

        if f == "9":
            print("Error")

        return a

    def measurement(self) -> float:
        """
        Measures height

        Returns height value or nan on bad read.
        """
        m: float = 0.0
        cmd = "1\r".encode()
        self.ser.write(cmd)
        a = self.answer().split("\r")[0]

        if a.startswith("1A"):
            try:
                m = float(a.replace("1A", ""))
            except ValueError:
                m = nan
        return m

    def info(self) -> str:
        cmd = "V\r".encode()
        self.ser.write(cmd)
        a = self.answer()

        return a

    def close(self) -> None:
        self.ser.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
