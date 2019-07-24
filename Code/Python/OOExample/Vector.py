'''
Created on Oct 16, 2014

@author: pmackenz
'''

class Vector(object):
    '''
    vector class implementation using lists
    
    variables:
        self.v ... vector components stored in a list
    
    methods:
        def __init__(self, v):
        def __str__(self):
        def __repr__(self):
        def __len__(self):
        def __getitem__(self, i):
        def __div__(self, x):
        def __add__(self, x):
        def __sub__(self, x):
        def __mul__(self, x):
        def dot(self,x):
        def cross(self,x):
    '''

    def __init__(self, v):
        '''
        Constructor
        '''
        self.v = v
        
    def __str__(self):
        return str(self.v)
    
    def __repr__(self):
        return repr(self.v)
    
    def __len__(self):
        return len(self.v)
    
    def __getitem__(self, i):
        return self.v[i]

    def __div__(self, x):
        raise NotImplemented
    
    def __add__(self, x):
        if type(x) == Vector:
            w = self.v[:]
            for i in range(0,len(self)):
                w[i] += x[i]
            return Vector(w)
        else:
            raise TypeError
        
    def __sub__(self, x):
        if type(x) == Vector:
            w = self.v[:]
            for i in range(0,len(self)):
                w[i] -= x[i]
            return Vector(w)
        else:
            raise TypeError
        
    def __mul__(self, x):
        return self.dot(x)

    def dot(self,x):
        if type(x) == Vector:
            w = 0.0
            for i in range(0,len(self)):
                w += self.v[i] * x[i]
            return w
        else:
            raise TypeError
        
    def cross(self,x):
        if type(x) == Vector:
            if len(self.v) == 3:
                w = [
                     self.v[1]*x[2] - self.v[2]*x[1],
                     self.v[2]*x[0] - self.v[0]*x[2],
                     self.v[0]*x[1] - self.v[1]*x[0]
                    ]
            elif len(self.v) == 2:
                w = self.v[0]*x[1] - self.v[1]*x[0]
            else:
                print "cross product not defined for vectors other than R3"
                raise TypeError
            return Vector(w)
        else:
            raise TypeError
        