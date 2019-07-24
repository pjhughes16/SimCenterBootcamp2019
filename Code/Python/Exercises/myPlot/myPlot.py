import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np

pi = np.pi
x = np.linspace(-pi, pi, 100)

plt.plot(x, np.sin(x), label='sine')
plt.plot(x, np.cos(x), label='cosine')
plt.plot(x, np.tan(x), label='tangent')

axes = plt.gca()
axes.set_xlim([-pi,pi])
axes.set_ylim([-pi,pi])

plt.xlabel('x')
plt.ylabel('y')
plt.title("Three Basic Trigonometric Functions")
plt.legend()

#plt.show()

ext = 'pdf'
figname = 'myPlot.' + ext
plt.savefig(figname)

