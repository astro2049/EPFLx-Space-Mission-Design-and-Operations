import math

g = 9.80665
Isp = 220
mRosetta = 3000
mF = mRosetta / 2

vE = Isp * g
maxDeltaV = vE * math.log(mRosetta / mF)
print(round(maxDeltaV / 1000, 2))

v = 100
mF1 = mRosetta / (math.exp(100 / vE))
print(mF1)
