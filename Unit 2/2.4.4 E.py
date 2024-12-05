import math

mu_Earth = 3.986e14
r_Earth = 6.378e6
R = r_Earth + 400e3
omega = math.sqrt(mu_Earth / R ** 3)
T = 2 * math.pi / omega
revs = round(24 * 3600 / T)

print(revs)
