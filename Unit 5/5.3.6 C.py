import math

mu_Earth = 3.986e14  # m^3 * s^-2, GM Earth
r_Earth = 6.378e6  # m, Earth radius (equatorial)

h = 296e3
v = math.sqrt(mu_Earth / (h + r_Earth))
B = 3e-5
l = 20e3
U = v * B * l
print(round(U / 1000, 2))
