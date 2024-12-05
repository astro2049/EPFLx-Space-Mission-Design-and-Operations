mu_Moon = 4.903e12
r_Moon = 1.738e6
gMoon = mu_Moon / (r_Moon ** 2)
r_Earth = 6.378e6
g = 9.80665
depth = r_Moon * gMoon / g
print(round(depth / 1000))
