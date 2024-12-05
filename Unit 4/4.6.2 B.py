import math

mu_Sun = 1.327e20
mu_Earth = 3.986e14
AU = 1.496e11

# 1
r1 = AU
r2 = 5.204 * AU
a = (r1 + r2) / 2
vDInf = math.sqrt(mu_Sun * (2 / r1 - 1 / a)) - math.sqrt(mu_Sun / AU)
print(round(vDInf / 1000, 2))

# 2
r_Earth = 6.378e6
hPark = 200e3
vE = math.sqrt(2 * mu_Earth / (r_Earth + hPark))
vD = math.sqrt(vDInf ** 2 + vE ** 2)
print(round(vD / 1000, 2))

# 3
eEscape = vDInf ** 2 / 2
print(round(eEscape / 1e6, 2))

# 4
eTransfer = -mu_Sun / (2 * a)
print(round(eTransfer / 1e6, 2))

# 5
T = 2 * math.pi * math.sqrt(a ** 3 / mu_Sun)
t = T / 2
print(round(t / 24 / 3600, 1))

# 6
vAInf = math.sqrt(mu_Sun * (2 / r2 - 1 / a)) - math.sqrt(mu_Sun / r2)
print(round(vAInf / 1000, 2))

# 7
mu_Jupiter = 1.267e17
closestH = 100000e3
vClosestPoint = math.sqrt(vAInf ** 2 + 2 * mu_Jupiter * (1 / closestH))
vCirc = math.sqrt(mu_Jupiter / closestH)
deltaVI = vCirc - vClosestPoint
print(round(deltaVI / 1000, 2))
