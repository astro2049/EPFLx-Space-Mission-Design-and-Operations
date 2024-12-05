import math

m0 = 4050
deltaV = 11.5e3 - 7.78e3
Isp = 320
g = 9.80665
vE = Isp * g
mF = m0 / math.exp(deltaV / vE)
t = (m0 - mF) / 5
print(round(t, 2))
