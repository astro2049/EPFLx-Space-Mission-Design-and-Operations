import math

mu_Sun = 1.327e20

AU = 1.496e11
a = (1 + 1.52) * AU / 2
T = 2 * math.pi * math.sqrt(a ** 3 / mu_Sun)
t = T / 2
print(round(t / 24 / 3600, 2))
