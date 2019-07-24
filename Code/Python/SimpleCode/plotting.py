import numpy
from matplotlib import pyplot

mu, sigma = 2, 0.5

v = numpy.random.normal(mu,sigma,10000)

pyplot.hist(v, bins=50, normed=1)       # matplotlib version (plot)
pyplot.show()

