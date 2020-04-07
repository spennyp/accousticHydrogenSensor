import numpy as np
import math
import matplotlib.pyplot as plt


voltage = np.linspace(0,10, 1000)


# Distance plot
distance = np.linspace(80, 300, 1000)
plt.clf()
plt.plot(distance, voltage)
plt.title("Sensor voltage reading vs distance in test vessel")
plt.xlabel("Distance (mm)")
plt.ylabel("Voltage (V)")
plt.xlim([0, 300])
plt.ylim([0, 11])
# plt.show()
plt.savefig("../Plots/voltageVsDistance.png")


# TOF plot
plt.clf()
gamma = 1.4
R = 8.31446261815324 # J/(K*mol)
M = 28.95 / 1000 # kg/mol for dry air

alpha = math.sqrt(M/gamma/R)

temperaturesC = [-40, 0, 20, 90]
temperaturesK = temperaturesC 
voltage = np.linspace(0, 10, 1000)

tofs = []

for i in range(0, len(temperaturesK)):
    tempC = temperaturesC[i]
    T = tempC + 273.15
    tof = (22*voltage+80)*alpha/math.sqrt(T)
    tofs.append((tof, tempC))
    plt.plot(tof, voltage, label=f"T = {tempC}$\xb0$C")

plt.title("Sensor voltage reading vs time of flight in test vessel")
plt.xlabel("Time of flight (*$10^{-3}$s)")
plt.ylabel("Voltage (V)")
plt.legend(loc="upper left")
# plt.xlim([0, 21])
# plt.ylim([0, 11])
# plt.show()
plt.savefig("../Plots/voltageVsTof.png")


# Velocity Plot
d = 300*10**(-3)
plt.clf()

for val in tofs:
    tof = val[0]
    tempC = val[1]
    v = d / tof
    plt.plot(v*1000, voltage, label=f"T = {tempC}$\xb0$C")

plt.title("Sensor voltage reading vs speed of sound in test vessel")
plt.xlabel("Speed of sound (m/s)")
plt.ylabel("Voltage (V)")
plt.legend(loc="upper right")
# plt.xlim([0, 21])
# plt.ylim([0, 11])
# plt.show()
plt.savefig("../Plots/voltageVsSos.png")


