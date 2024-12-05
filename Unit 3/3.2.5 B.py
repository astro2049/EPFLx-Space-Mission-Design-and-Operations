import math

mu_Earth = 3.986e14
r_Earth = 6.378e6

r1 = r_Earth + 230e3
r2 = r_Earth + 20000e3

v1 = math.sqrt((2 * mu_Earth * r2) / (r1 * (r1 + r2))) - math.sqrt(mu_Earth / r1)
v1 /= 1000
print(v1)
v2 = math.sqrt(mu_Earth / r2) - math.sqrt((2 * mu_Earth * r1) / (r2 * (r1 + r2)))
v2 /= 1000
print(v2)
