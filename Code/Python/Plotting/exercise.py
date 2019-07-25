import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 100)

plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.plot(x, np.tan(x), label='tan(x)')

plt.xlabel('x in radians')
#plt.ylabel('y label')

plt.grid(True, which='both')

plt.title("Trigonometric function")

plt.legend()

plt.ylim(top=3, bottom=-3)

#plt.show()

plt.savefig('trig.png')

