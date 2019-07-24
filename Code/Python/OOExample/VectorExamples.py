'''
Created on Oct 14, 2015

@author: pmackenz
'''

from Vector import *
#from VectorNoisy import *
#from VectorNumpy import *

# define two vectors
v = Vector([1, 2, 3])
w = Vector([4, 6, 8])

print "v:     {} generated as {}".format(v, repr(v))
print "w:     {}".format(w)

# addition
x = v + w
print "v + w: {}".format(x)
  
# subtraction  
y = v - w
print "v - w: {}".format(y)

# dot product
z = v * w
print "v * w: {}".format(z)
z = v.dot(w)
print "dot(v,w): {}".format(z)

# cross product
z = v.cross(w)
print "v x w: {}".format(z)

# combined operation product
z = v * (v + w)
print "v * (v + w): {}".format(z)
z = v.dot(v+w)
print "v.dot(v + w): {}".format(z)
