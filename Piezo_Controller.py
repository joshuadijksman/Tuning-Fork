"""
Integration of the E-625 Piezo Servo Controller from PI
"""

from pipython import GCSDevice
from threading import Thread
import threading
import time


class E625:
    def __init__(self, serialnum="121019479"):
        self.pidevice: GCSDevice = GCSDevice("E-625")
        # Serial number to connect to can be read on device!
        self.pidevice.ConnectUSB(serialnum)

        # Or use the dialog and you will read "E-816USB SN 121019479"
        # self.pidevice.InterfaceSetupDlg(key='sample')

        self.stopMutex = threading.Lock()
        self._stop = True

        self.target = "A"

    def servoloop(self, closed=False):
        self.pidevice.SVO(self.target, closed)

    def relative_voltage(self, voltage):
        self.pidevice.SVO(self.target, False)
        self.pidevice.SVR(self.target, voltage)

    def absolute_voltage(self, voltage):
        self.pidevice.SVO(self.target, False)
        self.pidevice.SVA(self.target, voltage)

    def request_voltage(self):
        return self.pidevice.qVOL(self.target)["A"]

    def thread_for_voltage(self, start, end, step, waittime):
        v = start

        while v < end:
            with self.stopMutex:
                if self._stop:
                    break
            self.absolute_voltage(v)

            v = v + step
            time.sleep(waittime)

        self.stop()

    def stop(self):
        # Must protect self._stop with a mutex because a secondary thread
        # might try to access it at the same time.
        print("*")
        with self.stopMutex:
            if not self._stop:
                self._stop = True

    def for_voltage(self, start, end, step, waittime):
        # Must protect self._stop with a mutex because a secondary thread
        # might try to access it at the same time.
        # if a thread is already running do not start a second one!!!
        with self.stopMutex:
            if self._stop:
                self._stop = False
                ok_to_start = True
            else:
                ok_to_start = False

        if ok_to_start:
            self.for_task = Thread(
                target=self.thread_for_voltage,
                args=(
                    start,
                    end,
                    step,
                    waittime,
                ),
            )

            self.for_task.start()

    def close(self):
        self.pidevice._cleanup()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
