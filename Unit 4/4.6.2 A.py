import math

mu_Sun = 1.327e20
AU = 1.496e11

# 1
vI = math.sqrt(17e3 ** 2 + 2 * mu_Sun * (1 / AU - 1 / (133.9 * AU)))
print(round(vI / 1000, 2))
