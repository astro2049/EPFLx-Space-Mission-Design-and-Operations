import math

mu_Sun = 1.327e20
mu_Earth = 3.986e14
r_Earth = 6.378e6
AU = 1.496e11

vD = 11e3  # departure velocity
rPark = 1000e3 + r_Earth

# 1
epsilon = vD ** 2 / 2 - mu_Earth / rPark
rSOI = AU * (mu_Earth / mu_Sun) ** (2 / 5)
vS = math.sqrt(2 * (epsilon + mu_Earth / rSOI))
print(round(vS / 1000, 2))

# 2
vEscape = math.sqrt(2 * mu_Earth / rPark)
vInf = math.sqrt(vD ** 2 - vEscape ** 2)
print(round(vInf / 1000, 2))
