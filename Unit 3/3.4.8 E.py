import math

deltaR = 12e3
deltaX = 3 * math.pi * deltaR
rounds = round(400e3 / deltaX, 2)
print(rounds)
