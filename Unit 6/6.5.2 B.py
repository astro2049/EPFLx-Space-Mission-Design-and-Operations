import math

mu_Earth = 3.986e14
r_Earth = 6.378e6
hCoG = 296e3
hSat = 315.9e3
RCoG, RSat = hCoG + r_Earth, hSat + r_Earth
omega = math.sqrt(mu_Earth / RCoG ** 3)
vSat = omega * RSat
a = 1 / (2 / RSat - vSat ** 2 / mu_Earth)
print(round((a - RSat) / 1000, 2))
