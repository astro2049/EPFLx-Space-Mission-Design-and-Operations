import math

g = 9.80665


def deltaV(Isp, m0, mF):
    return Isp * g * math.log(m0 / mF)


# 1
print(round((deltaV(311, 260 + 53 + 10, 20 + 53 + 10) + deltaV(342, 53 + 10, 3 + 10)) / 1000, 2))

# 2
print(round(deltaV(342, 313 + 10, 23 + 10) / 1000, 2))
