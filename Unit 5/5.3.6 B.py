S = 1.361e3  # W * m^-2 at 1 AU, Solar Constant
T = 90 * 60
consumePower = 500
tSun, tShadow = T * 0.6, T * 0.4
eShadow = tShadow * consumePower
chargingRate = eShadow / tSun
power = consumePower + chargingRate
area = power / (S * 0.25)
print(round(area, 1))
