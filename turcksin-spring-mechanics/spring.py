import json

with open("settings.json", 'r') as f:
    settings = json.loads(f.read())


print settings["spring_constant"]



# example for ODE solver:

from scipy.integrate import ode
import numpy as np
import matplotlib.pyplot as plt

D = 52.
L = 2.25
g = [0.,0.,-9.81]

# variable order:
# p1x p1y p1z p2x p2y p2z v1x v1y v1z v2x v2y v2z

y0 = [1.,2.,3., 4.,5.,6., 0.,0.,0., 1.,1.,1.]
t0 = 0.
T = 0.5

m = [3.0, 1.0]


def f(t, y):
    p1 = y[0:3]
    p2 = y[3:6]
    v1 = y[6:9]
    v2 = y[9:12]
    
    dist = np.linalg.norm(p2-p1)
    a1 = g - D*(dist-L) * (p2-p1)/dist/m[0];
    a2 = g - D*(dist-L) * (p1-p2)/dist/m[1];
    return np.concatenate([v1, v2, a1, a2])             

r = ode(f).set_integrator('vode',rtol=1e-6)
r.set_initial_value(y0, t0)

t = [t0]
yarr = np.array([y0])

while r.successful() and r.t < T:
    r.integrate(T, step=True)
    t.append(r.t)
    yarr = np.vstack((yarr,r.y))

print "time steps:",len(t)


plt.plot(t, yarr[:,0],
         t, yarr[:,1],
         t, yarr[:,2],
         t, yarr[:,3],
         t, yarr[:,4],
         t, yarr[:,5])

plt.legend(["p1.x","p1.y", "..."])

plt.show()
