import numpy as np
import math
import matplotlib.pyplot as plt

tCelcius = np.linspace(-40, 90, 300)
T = tCelcius + 273.15 # K
R = 8.31446261815324 # J/(K*mol)

# Molar Mass in kg / mol
MH = 1.00784 / 1000 * 2
MN = 14.0067 / 1000 * 2
MHe = 4.002602 / 1000

# Specific heat at constant pressure in in J/(K*mol)
cpH = 14.32 * MH * 1000
cpN = 1.04 * MN * 1000
cpHe = 5.19 * MHe * 1000

pctH = np.linspace(0, 1, 5)
pctN = np.linspace(1, 0, 5)

concentrations = list(zip(pctH, pctN))

# With hydrogen
for concentration in concentrations:
    pctH = concentration[0]
    pctN = concentration[1]
    numerator = R*T*(pctH*cpH + pctN*cpN)
    denominator = (pctH*MH + pctN*MN) * (pctH*(cpH - R) + pctN*(cpN - R))
    v = np.sqrt(numerator/denominator)
    plt.plot(tCelcius, v, label=f"$x_H$ = {pctH}, $x_N$ = {pctN}")

plt.title("Speed of sound in H, N gas mixture")
plt.xlabel("Temperature (C)")
plt.ylabel("Speed of sound (m/s)")
plt.ylim([0, 2000])
plt.legend(loc="upper left")
# plt.show()
plt.savefig("../Plots/sosGasMixtureVsTempH.png")


# With helium (some concentrations)
plt.clf()
for concentration in concentrations:
    pctHe = concentration[0]
    pctN = concentration[1]
    numerator = R*T*(pctHe*cpHe + pctN*cpN)
    denominator = (pctHe*MHe + pctN*MN) * (pctHe*(cpHe - R) + pctN*(cpN - R))
    v = np.sqrt(numerator/denominator)
    plt.plot(tCelcius, v, label=f"$x_{{He}}$ = {pctHe}, $x_N$ = {pctN}")

plt.title("Speed of sound in He, N gas mixture")
plt.xlabel("Temperature (C)")
plt.ylabel("Speed of sound (m/s)")
plt.ylim([0, 2000])
plt.legend(loc="upper left")
# plt.show()
plt.savefig("../Plots/sosGasMixtureVsTempHe.png")