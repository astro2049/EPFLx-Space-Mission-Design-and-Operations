import math

aDeflect = 27 * math.pi / 180
a = 6.2 * math.sin(aDeflect)
b = 6.2 * math.cos(aDeflect)
c = 35.2
print(round(math.sqrt((a + c) ** 2 + b ** 2), 2))
