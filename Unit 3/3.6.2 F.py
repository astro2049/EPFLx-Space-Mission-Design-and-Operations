import math

Sidereal_day = 86164.09
mu_Earth = 3.986e14
r_Earth = 6.378e6

T = Sidereal_day
omega = 2 * math.pi / T
r = (mu_Earth / omega ** 2) ** (1 / 3)
print(r / 1000)
