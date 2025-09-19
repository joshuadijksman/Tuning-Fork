##  The available commands are:
##  Sf (x);   | This command sets the normal frequency to x (note that if the frequency controller is engaged this value will be overwritten)
##  Rf;       | This command returns the current normal frequency
##  Sa (x);   | This command sets the normal sine out amplitude to x (note that if the amplitude controller is engaged this value will be overwritten)
##  Ra;       | This command returns the current normal sine out amplitude
##  Ssa (x);  | This command sets the amplitude setpoint for the normal amplitude controller to x
##  Rsa;      | This command returns the current normal amplitude setpoint for the amplitude controller
##  Rp;       | This command returns the current normal phase
##  Ef (X);   | This command enables or disables the normal frequency controller (x = 1 enables the controller and x = 2 disables the controller)
##  Ea (X);   | This command enables or disables the normal amplitude controller (x = 1 enables the controller and x = 2 disables the controller)
##  Ed (X);   | This command enables or disables the data stream (x = 1 enables the stream and x = 2 disables the stream)
##  SCe (X);  | This command sets the exponential term for the normal frequency controller
##  SCl (X);  | This command sets the linear term for the normal frequency controller
##  SCp (X);  | This command sets both exponential and linear terms for the normal frequency controller (1 = open air, 2 = 20 cSt, 3 = 500 cSt, 4 = 10 000 cSt, 5 = 30 000 cSt)
##  SCAl (X); | This command sets the linear term for the normal amplitude controller
##  SCAp (X); | This command sets the linear term for the normal amplitude controller (preset 1 is most conservative and preset 5 is most agressive)

import time
import serial

from serial.tools import list_ports

def find_unique_dev_by_pidvid(pid: int, vid: int):
     found_devices = list(filter(lambda p: p.pid == pid and p.vid == vid, list_ports.comports()))
     return found_devices[0] if len(found_devices) == 1 else None


class sfa():

    def __init__(self, PID=0x7523, VID=0x1A86):
        
        port = str(find_unique_dev_by_pidvid(pid=PID, vid=VID)).split(" ")[0]
        self.ser = serial.Serial(port, baudrate=9600,timeout=20)
        self.Sa(0.006)
        
    def write(self,cmd):

        senddata = cmd  + '\n\r'
        self.ser.write(senddata.encode())
        return


    def write_read(self,cmd):
        self.write(cmd)

        kar = self.ser.read().decode()
        terug = kar
        while kar != '\r':
            kar = self.ser.read().decode()
            terug = terug + kar
        terug = terug.strip()  
        return terug


    ##  Sf (x);   | This command sets the normal frequency to x (note that if the frequency controller is engaged this value will be overwritten)
    def Sf (self,x):

        command = "FREQ " + str(round(x,6))
        self.write(command)

    ##  Rf;       | This command returns the current normal frequency
    def Rf(self):

        command = "FREQ?"
        feedback = self.write_read(command)
        return float(feedback)

    ##  Sa (x);   | This command sets the normal sine out amplitude to x (note that if the amplitude controller is engaged this value will be overwritten)
    def Sa (self,x):

        self.sine_out_amplitude = round(x,6)
        command = "SLVL "  + str(self.sine_out_amplitude)
        
        self.write(command)

    def Rm(self):
        
        rawA = self.write_read("outp? 4")
      #  try:
        amp = round(float(rawA),6)
      #  except ValueError:
      #      amp = 0.0
        return amp
        

    ##  Ra;       | This command returns the current normal sine out amplitude
    def Ra (self):
        
        return self.sine_out_amplitude

    ##  Rp;       | This command returns the current normal phase
    def Rp (self):
        
        command = "OUTP? 3"
        feedback = self.write_read(command)
        return float(feedback)


##    ##  Ssa (x);  | This command sets the amplitude setpoint for the normal amplitude controller to x
##    def Ssa (self,x):
##        self.write('Ssa ' + str(x))
##
##    ##  Rsa;      | This command returns the current normal amplitude setpoint for the amplitude controller
##    def Rsa (self):
##        return self.write_read("Rsa").replace("normal amplitude setpoint = ","")

##
##    ##  SCe (X);  | This command sets the exponential term for the normal frequency controller
##    def SCe (self,x):
##        self.write('SCe ' + str(x))
##
##    ##  SCl (X);  | This command sets the linear term for the normal frequency controller
##    def SCl (self,x):
##        self.write('SCl ' + str(x))
##
##    ##  SCp (X);  | This command sets both exponential and linear terms for the normal frequency controller (1 = open air, 2 = 20 cSt, 3 = 500 cSt, 4 = 10 000 cSt, 5 = 30 000 cSt)
##    def SCp (self,x):
##        return self.write_read('SCp ' + str(x))
##
##    ##  SCAl (X); | This command sets the linear term for the normal amplitude controller
##    def SCAl (self,x):
##        self.write('SCAl ' + str(x))
##
##    ##  SCAp (X); | This command sets the linear term for the normal amplitude controller (preset 1 is most conservative and preset 5 is most agressive)
##    def SCAp (self,x):
##        return self.write_read('SCAp ' + str(x))
##

if __name__ == '__main__':

    s = sfa()

    time.sleep(2)
    s.Sf(1021.02)
    time.sleep(2)
    print("Rf:", s.Rf())
    print("Rm:", s.Rm())
    print("Rp:", s.Rp())
    print("end")

    s.ser.close()
