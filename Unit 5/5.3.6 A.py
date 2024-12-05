import math

mu_Earth = 3.986e14  # m^3 * s^-2, GM Earth
r_Earth = 6.378e6  # m, Earth radius (equatorial)
Sidereal_day = 86164.09  # s, 23h 56min 04.09sec

T = Sidereal_day
R = ((T / (2 * math.pi)) ** 2 * 2 * mu_Earth) ** (1 / 3)
h = R - r_Earth
print(round(h / 1000))
