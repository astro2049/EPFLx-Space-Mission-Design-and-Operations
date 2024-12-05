import math

mu_Earth = 3.986e14
r_Earth = 6.378e6
hISS = 400e3
hPeri = 200e3
R2, R1 = hISS + r_Earth, hPeri + r_Earth
deltaV = math.sqrt(mu_Earth / R2) - math.sqrt(2 * mu_Earth * R1 / (R2 * (R1 + R2)))
print(round(deltaV, 2))

m = 2 * 8.9 / deltaV
print(round(m, 2))
