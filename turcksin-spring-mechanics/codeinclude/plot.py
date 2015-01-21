import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D
fig = matplotlib.pyplot.figure()
canvas = fig.gca(projection='3d')
canvas.plot(y_values[:,0], y_values[:,1], y_values[:,2],
            label='body 1')
canvas.plot(y_values[:,3], y_values[:,4], y_values[:,5], 
            label='body 2')
canvas.legend()
matplotlib.pyplot.show()
