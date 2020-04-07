import numpy as np
import math
import matplotlib.pyplot as plt

hydrogen = False

temps = np.linspace(-45 + 273.15, 90 + 273.15, 300)
R = 8.31446261815324

gammaAir = 1.4
gammaN = 1.4
gammaH = 1.4
gammaH2Ov = 1.33
gammaHe = 1.67

MN = 14.0067 / 1000 * 2
MH = 1.00784 / 1000 * 2
MH2Ov = 18.01528 / 1000
MHe = 4.002602 / 1000
Mair = 28.95 / 1000 # kg/mol for dry air

vN = np.sqrt(gammaN*R*temps/MN)
vH = np.sqrt(gammaH*R*temps/MH)
vH2Ov = np.sqrt(gammaH2Ov*R*temps/MH2Ov)
vHe = np.sqrt(gammaHe*R*temps/MHe)
vAir = np.sqrt(gammaAir*R*temps/Mair)

temps = temps - 273.15

# All on the same plot
plt.plot(temps, vH, label=f"Hydrogen")
plt.plot(temps, vHe, label=f"Helium")
plt.plot(temps, vN, label=f"Nitrogen")
plt.plot(temps, vH2Ov, label=f"Water Vapor")
# plt.plot(temps, vAir, label=f"Air")
plt.title("Speed of sound in gases")
plt.xlabel("Temperature (C)")
plt.ylabel("Speed of sound (m/s)")
plt.ylim([0, 2000])
plt.xlim([-40, 90])   
plt.legend(loc="upper left")
# plt.show()
plt.savefig("../Plots/sosIndividualGassesVsTemp.png")

vFastest = math.sqrt(gammaH*R*(90+273.15)/MH)
print(vFastest)
