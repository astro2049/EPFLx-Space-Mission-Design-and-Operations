import math

r_Earth = 6.378e6  # m, Earth radius (equatorial)
Sidereal_day = 86164.09  # s, 23h 56min 04.09sec

omega = 2 * math.pi / Sidereal_day
v = omega * r_Earth
print(round(v, 2))
