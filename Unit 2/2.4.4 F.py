import math

mu_Earth = 3.986e14
r_Earth = 6.378e6

a = (20000e3 + r_Earth) / 1.3
r = 0.7 * a

v = math.sqrt(mu_Earth * ((2 / r) - (1 / a)))

print(v / 1000)
