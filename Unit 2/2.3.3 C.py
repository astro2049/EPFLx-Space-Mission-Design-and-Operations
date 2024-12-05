import math

mu_Earth = 3.986e14
Sidereal_day = 86164.09

a = (mu_Earth * (Sidereal_day / (2 * math.pi)) ** 2) ** (1 / 3)

r_Earth = 6.378e6
print((a - r_Earth) / 1000)
