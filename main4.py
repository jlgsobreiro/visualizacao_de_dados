import matplotlib.pyplot as plt
import numpy as np

co_ = 0.25 * 10.0**(-3)
g = 6*10**(4)
k = 2 * 10**(3)
kt = 0.9 * 10**(-9)
n = 5 * 10**(2)

ca0 = 0.2
co0 = 0.0
cp0 = 0.0

ra = -k * ca0**n * co0**n
ro = (1/2)*ra
rp = -(1/2)*ra
kla = kt * n**3 * g ** (1/2)

vdcadt = lambda v: ra*v
vdcodt = lambda v: kla * (co_ - co0)*v - ro*v
vdcpdt = lambda v: rp*v

ca0 = 0.1
k = 1.3
cb0 = 0

dCa_dt = lambda n: -k * ca0 ** n
dCb_dt = lambda n: k * ca0 ** n

xat = lambda n, cx: (ca0 - cx(n)) / ca0

x = np.arange(0, 2, 0.01)
y = [xat(x, dCa_dt) for x in x]
z = [xat(x, dCb_dt) for x in x]

plt.plot(x, z)
plt.plot(x, y)
plt.title('Simple plot')
plt.show()
