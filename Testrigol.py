import serial
import time
import numpy as np
import csv
import matplotlib.pyplot as plt
import newsfa as sfa

# ---------------------------
# Instellingen COM-poorten
# ---------------------------
# Pas deze COM-poorten aan (Windows: COM3, COM4; Linux/Mac: /dev/ttyUSB0 etc.)
rigol_port = 'COM3'
sr830_port = 'COM4'

ctrlNormal: sfa.sfa = sfa.sfa(SN="A9JSTXTQA")
ctrlShear: sfa.sfa = sfa.sfa(SN="A9TQAG5OA")


# Rigol instellingen
rigol = serial.Serial(rigol_port, baudrate=9600, timeout=1)
time.sleep(1)  # even wachten tot verbinding stabiel is

# SR830 instellingen

# ---------------------------
# Rigol setup
# ---------------------------
def rigol_write(cmd):
    rigol.write((cmd + '\n').encode())

def rigol_query(cmd):
    rigol.write((cmd + '\n').encode())
    time.sleep(0.1)
    return rigol.read(200).decode().strip()

print("Rigol IDN:", rigol_query('*IDN?'))

rigol_write('FUNC SIN')
rigol_write('VOLT 1')
rigol_write('OUTP ON')


# ---------------------------
# Sweep parameters
# ---------------------------
f_start = 32760
f_stop = 32780
f_step = 0.1   # let op: niet te klein beginnen, test eerst 0.1 Hz stappen
delay = 0.3    # moet ~3–10× de time constant van SR830 zijn

frequencies = np.arange(f_start, f_stop + f_step, f_step)

amplitudes = []
phases = []

# ---------------------------
# Sweep loop
# ---------------------------
for f in frequencies:
    rigol_write(f"FREQ {f}")
    time.sleep(delay)

    R = ctrlNormal.Rm()
    Theta = ctrlNormal.Rp()

    try:
        R_val = float(R)
    except:
        R_val = np.nan
    try:
        T_val = float(Theta)
    except:
        T_val = np.nan

    amplitudes.append(R_val)
    phases.append(T_val)

    print(f"f={f:.2f} Hz, R={R_val}, θ={T_val}")

# ---------------------------
# Data opslaan
# ---------------------------
with open("sweep_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Frequency (Hz)", "Amplitude R (V)", "Phase θ (deg)"])
    for i in range(len(frequencies)):
        writer.writerow([frequencies[i], amplitudes[i], phases[i]])

print("Data opgeslagen in sweep_data.csv")

# ---------------------------
# Plot
# ---------------------------
plt.figure()
plt.plot(frequencies, amplitudes, label="Amplitude R")
plt.xlabel("Frequentie (Hz)")
plt.ylabel("Amplitude (V)")
plt.title("Resonantiecurve stemvork")
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.plot(frequencies, phases, label="Fase θ")
plt.xlabel("Frequentie (Hz)")
plt.ylabel("Fase (graden)")
plt.title("Fase respons SR830")
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------
# Sluit verbindingen
# ---------------------------
rigol.close()
