# read input file
import sys
import json

assert len(sys.argv)==2, 'Please provide an input file.'
with open(sys.argv[1], 'r') as f:
    settings = json.loads(f.read())


# example for ODE solver:

from scipy.integrate import ode
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

D = settings['spring constant']
L = settings['spring rest length']
g = [0., 0., -9.81]

# variable order:
# p1x p1y p1z p2x p2y p2z v1x v1y v1z v2x v2y v2z

init_p1 = settings['initial position'][0]
init_p2 = settings['initial position'][1]
init_v1 = settings['initial velocity'][0]
init_v2 = settings['initial velocity'][1]
y0 = [init_p1[0], init_p1[1], init_p1[2], init_p2[0], init_p2[1], init_p2[2],\
        init_v1[0], init_v1[1], init_v1[2], init_v2[0], init_v2[1], init_v2[2]]
t0 = 0.
T = 2

m = [settings['masses'][0], settings['masses'][1]]


def f(t, y):
    p1 = y[0:3]
    p2 = y[3:6]
    v1 = y[6:9]
    v2 = y[9:12]

    dist = np.linalg.norm(p2-p1)
    a1 = g - D*(dist-L) * (p1-p2)/dist/m[0]
    a2 = g - D*(dist-L) * (p2-p1)/dist/m[1]
    return np.concatenate([v1, v2, a1, a2])

r = ode(f).set_integrator('vode', rtol=1e-6)
r.set_initial_value(y0, t0)

t = [t0]
yarr = np.array([y0])

while r.successful() and r.t < T:
    r.integrate(T, step=True)
    t.append(r.t)
    yarr = np.vstack((yarr, r.y))

print "time steps:", len(t)


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(yarr[:,0], yarr[:,1], yarr[:,2], label='body 1')
ax.plot(yarr[:,3], yarr[:,4], yarr[:,5], label='body 2')

plt.show()
