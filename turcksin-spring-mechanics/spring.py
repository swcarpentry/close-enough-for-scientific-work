import json

with open("settings.json", 'r') as f:
    settings = json.loads(f.read())


print settings["spring_constant"]



# example for ODE solver:

from scipy.integrate import ode
import numpy as np
import matplotlib.pyplot as plt

y0 = [80, 30]
t0 = 0
T = 100

def f(t, y):
    return [0.125*y[0]-0.01*y[0]*y[1], -y[1]+0.01*y[0]*y[1]]

r = ode(f).set_integrator('vode',rtol=1e-8)
r.set_initial_value(y0, t0)

tarr = []
y1arr = []
y2arr = []

while r.successful() and r.t < T:
    r.integrate(T, step=True)
    tarr.append(r.t)
    y1arr.append(r.y[0])
    y2arr.append(r.y[1])

print len(tarr)

#plt.plot(tarr, y1arr, 'yo-', tarr, y2arr, 'rx-')
plt.plot(y1arr, y2arr, 'r-')
plt.show()
