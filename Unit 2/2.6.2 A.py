import math

R_FG3 = 700
mu_FG3 = 140.15
r1 = 1.5e3

# 1
v = math.sqrt(mu_FG3 / (r1 + R_FG3))
print(v)

# 2
a = (r1 + R_FG3 + 10) / 2

n = math.sqrt(mu_FG3 / a ** 3)  # mean motion, rad/s
T = 2 * math.pi / n  # period

e = (a - 10) / a  # eccentricity
E = (360 - 68.08) * math.pi / 180  # eccentric anomaly
t = (E - e * math.sin(E)) / n  # Kepler's equation

print((t - T / 2) / 3600)

# 3
theta = 191.35 * math.pi / 180  # true anomaly

r2 = (10 * (1 + e)) / (1 + e * math.cos(theta))
vLand = math.sqrt(mu_FG3 * (2 / r2 - 1 / a))  # Vis-viva equation

print(vLand)

# 4
gamma = math.atan((e * math.sin(theta)) / (1 + e * math.cos(theta)))
print(gamma * 180 / math.pi)

# 5
g = mu_FG3 / R_FG3 ** 2
tLand = 2 * math.sqrt(2 * vLand / g)
print(tLand)
