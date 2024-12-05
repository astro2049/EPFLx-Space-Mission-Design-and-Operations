MCass = 5600
hCass = 5
dCass = 2
mAntenna = 50
lArm = 10

rCass = dCass / 2
I1 = 1 / 2 * MCass * rCass ** 2 + 2 * mAntenna * rCass ** 2
omega = 6
L = I1 * omega
I2 = 1 / 2 * MCass * rCass ** 2 + 2 * mAntenna * (rCass + lArm) ** 2
print(L / I2)
