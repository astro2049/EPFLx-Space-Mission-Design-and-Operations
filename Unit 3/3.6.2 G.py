import math

mu_Earth = 3.986e14
r_Earth = 6.378e6

r1 = 350e3 + r_Earth
r2 = r_Earth + 400e3

deltaV1 = math.sqrt((2 * mu_Earth * r2) / (r1 * (r1 + r2))) - math.sqrt(mu_Earth / r1)
print(deltaV1)
