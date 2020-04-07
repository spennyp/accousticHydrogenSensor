import math
import numpy as np
import matplotlib.pyplot as plt

hydrogen = False

name = "hydrogen" if hydrogen else "helium"
symbol = "H" if hydrogen else "He"
deltaX = 0.001

xVals = np.linspace(0, 1, int(1/deltaX))

R = 8.31446261815324 # J/(K*mol)
M = 28.95 / 1000 # kg/mol for dry air
gamma = 1.4
d = 300*10**(-3)

# Molar Mass in kg / mol
MH = 4.002602 / 1000 # Helium
if hydrogen:
    MH = 1.00784 / 1000 * 2 # Hydrogen
MN = 14.0067 / 1000 * 2

# Thermal heat capacity 
cH = 5.1926 * MH * 1000 # Helium
if hydrogen:
    cH = 14.307 * MH * 1000 # Hydrogen
cN = 1.039 * MN * 1000

alpha = math.sqrt(M/gamma/R)
A = cH - cN
B = cN
C = MH - MN
D = MN
E = cH - cN
F = cN - R
G = C*E
H = C*F+D*E
I = D*F

print(f"{A}, {B}, {G}, {H}, {I}")

def voltage(x):
    return 1/22*(300/alpha/math.sqrt(R)*math.sqrt((G*x**2 + H*x + I) / (A*x+B)) - 80)

vVals = []

for x in xVals:
    vVals.append(voltage(x))
    

# %H vs volgage
plt.plot(np.array(vVals), xVals * 100)
plt.title(f"Concentration of {name} in {symbol}, N mixture vs Voltage")
plt.ylabel(f"%{symbol}")
plt.xlabel("V")
plt.ylim([0, 100])
plt.xlim([0, 10])
plt.savefig(f"../Plots/1compositionVsVoltage{symbol}.png")
# plt.show()


# voltage vs %H
plt.clf()
plt.plot(xVals * 100, np.array(vVals))
plt.title(f"Voltage vs concentration of {name} in {symbol}, N mixture ")
plt.xlabel(f"%{symbol}")
plt.ylabel("V")
plt.xlim([0, 100])
plt.ylim([0, 10])
plt.savefig(f"../Plots/1voltageVsComposition{symbol}.png")
# plt.show()


# numerical derivative
dvdxVals = []
for i in range(0, len(vVals) - 1):
    dvdxVals.append((vVals[i+1] - vVals[i])/deltaX)

dvdxVals.append(dvdxVals[-1]) # To make sizes agree
plt.clf()
plt.plot(xVals * 100, dvdxVals)
plt.title(f"dv/dx vs concentration (x) of {name} in {symbol}, N mixture")
plt.xlabel(f"%{symbol}")
plt.ylabel("dv/dx")
plt.xlim([0, 100])
plt.savefig(f"../Plots/1dvdxVsComposition{symbol}.png")
# plt.show()


# Error analysis
def vMin(v):
    return 0.99*v - 3.2*10**(-3)


def vMax(v):
    return 1.01*v + 3.2*10**(-3)

vMinVals = []
vMaxVals = []

print(vVals)

for v in vVals:
    vMinVals.append(vMin(v))
    vMaxVals.append(vMax(v))

plt.clf()
plt.plot(vVals, xVals * 100)
plt.plot(vMinVals, xVals*100, label="Lower error bound")
plt.plot(vMaxVals, xVals*100, label="Higher error bound")
plt.title(f"Concentration of {name} in {symbol}, N mixture vs Voltage with Error bounds")
plt.ylabel(f"%{symbol}")
plt.xlabel("V")
plt.legend(loc="lower left")

# plt.show()

plt.savefig(f"../Plots/1compositionVsVoltageError{symbol}.png")





