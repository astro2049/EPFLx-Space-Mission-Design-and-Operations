import math

mu_Earth = 3.986e14
r_Earth = 6.378e6

# 1
a = (210e3 + 2 * r_Earth + 590e3) / 2
T = 2 * math.pi * math.sqrt(a ** 3 / mu_Earth)
print(round(T / 2 / 60, 2))

# 2
t = T / 2
rSat = 590e3 + r_Earth
nSat = math.sqrt(mu_Earth / rSat) / rSat
nSat = nSat * 180 / math.pi  # rad to deg
sSat = nSat * t
print(180 - sSat)
