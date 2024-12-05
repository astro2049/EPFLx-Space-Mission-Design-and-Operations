import math

mu_Earth = 3.986e14
r_Earth = 6.378e6

r1 = r_Earth + 450e3
r2 = r_Earth + 35786e3

vLEO = math.sqrt(mu_Earth / r1)
print(vLEO / 1000)
vGEO = math.sqrt(mu_Earth / r2)
print(vGEO / 1000)

v1 = math.sqrt((2 * mu_Earth * r2) / (r1 * (r1 + r2))) - math.sqrt(mu_Earth / r1)
print(v1 / 1000)
v2 = math.sqrt(mu_Earth / r2) - math.sqrt((2 * mu_Earth * r1) / (r2 * (r1 + r2)))
print(v2 / 1000)
