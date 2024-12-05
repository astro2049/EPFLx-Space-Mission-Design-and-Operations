import math

omega = 2 * math.pi / 60
m = 2000 + 250
r = 1.1
I = 1 / 2 * m * r ** 2
thrusters = 2
F = 10.6
L = 0.5
t = I * omega / (thrusters * F * L)
print(round(t, 2))
