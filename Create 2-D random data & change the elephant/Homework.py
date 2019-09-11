# coding:utf-8
## draw an elephant
def fourier(t, C):
    f = zeros(t.shape)
    for k in range(len(C)):
        f += C.real[k] * cos(k * t) + C.imag[k] * sin(k * t)
    return f
def elephant(t, p):
    npar = 6
    Cx = zeros((npar,), dtype='complex')
    Cy = zeros((npar,), dtype='complex')
    Cx[1] = p[0].real * 1j
    Cy[1] = p[3].imag + p[0].imag * 1j
    Cx[2] = p[1].real * 1j
    Cy[2] = p[1].imag * 1j
    Cx[3] = p[2].real
    Cy[3] = p[2].imag * 1j
    Cx[5] = p[3].real
    x = append(fourier(t, Cy), [p[4].imag])
    y = -append(fourier(t, Cx), [-p[4].imag])
    return x, y
def init_plot():
    # draw the body of the elephant
    # create trunk
    x, y = elephant(linspace(2.9 * pi, 0.4 + 3.3 * pi, 1000), parameters)
    x, y = elephant(linspace(40 * pi, 0.4 + 100 * pi, 1000), parameters)
    for ii in range(len(y) - 1):
        y[ii] -= sin(((x[ii] - x[0]) * 2*pi / len(y))) * sin(float(0)) * parameters[4].real
    trunk.set_data(x, y)
    return trunk,

import matplotlib
matplotlib.use('TKAgg')
from matplotlib import animation
import matplotlib.pyplot as plt
from numpy import append, cos, linspace, pi, sin, zeros

def move_trunk(i):
    x, y = elephant(linspace(2.9 * pi, 0.4 + 3.3 * pi, 1000), parameters)
    for ii in range(len(y) - 1):
        y[ii] -= sin(((x[ii] - x[0]) * pi / len(y))) * sin(float(i)) * parameters[4].real
    trunk.set_data(x, y)
    return trunk,
fig, ax = plt.subplots()

# elephant parameters PLEASE NOTE IN SPYDER YOU SHOULD DISABLE THE ACTIVE SUPPORT in PREFs
#parameters = [50 - 30j, 18 + 8j, 12 - 10j, -14 - 60j, 20 + 20j]
parameters = [70 - 30j, 60+ 8j, 40 - 10j, -14 - 60j, 20 + 20j]
# initial the elephant body
x, y = elephant(t=linspace(0.4 + 1.3 * pi, 2.9 * pi, 1000), p=parameters)
plt.plot(x, y, 'b.')
plt.xlim([-75, 90])
plt.ylim([-70, 87])
plt.axis('off')
trunk, = ax.plot([], [], 'b.') # initialize trunk
ani = animation.FuncAnimation(fig=fig,
func=move_trunk,
frames=1000,
init_func=init_plot,
interval=500,
blit=False,
repeat=True)
plt.show()


## create a random vector
import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sampleNo = 100000;
#mu = [0, 3]
mu = [1]
Sigma = np.array([[3, 0.1], [0.1, 1]])
R = cholesky(Sigma)
s = np.dot(np.random.randn(sampleNo, 2), R) + mu
plt.plot()
plt.hist(s, 100, density=True)
plt.show()

s  = pd.DataFrame(s )
sns.pairplot(data=s)
plt.show()




