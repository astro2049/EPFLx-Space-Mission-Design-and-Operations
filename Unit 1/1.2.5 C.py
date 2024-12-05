import math

mu_Earth = 3.986e14
r_Earth = 6.378e6

# rGeo = r_Earth + 3.6e7
# vGeo = (2 * math.pi * rGeo) / (24 * 60 * 60)
# KGeo = 1 / 2 * vGeo ** 2
# KGeo should be ruled out!

print(math.sqrt(2 * mu_Earth * (-1 / (r_Earth + 3.6e7) + 1 / (r_Earth + 1e5))) / 1000)
