'''
Created on Oct 16, 2014

@author: pmackenz
'''

class Vector(object):
    '''
    verbose vector class implementation using lists
    
    variables:
        self.v
    
    methods:
        def __init__(self, v):
        def asarray(self):
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
        def Log(self,s):
    '''

    def __init__(self, v):
        self.Log("__init__(%s)" % v)
        '''
        Constructor
        '''
        self.v = v
        
    def __str__(self):
        self.Log("%s.__str__()" % self.v)
        return str(self.v)
    
    def __repr__(self):
        self.Log("%s.__repr__()" % self.v)
        return "Vector({})".format(self.v)
    
    def __len__(self):
        self.Log("%s.__len__()" % self.v)
        return len(self.v)
    
    def __getitem__(self, i):
        self.Log("%s.__getitem__(%i)" % (self.v,i))
        return self.v[i]

    def __div__(self, x):
        self.Log("%s.__div__(%s)" % (self.v,x))
        raise NotImplemented
    
    def __add__(self, x):
        self.Log("%s.__add__(%s)" % (self.v,x))
        if type(x) == Vector:
            w = self.v[:]
            for i in range(0,len(self)):
                w[i] += x[i]
            return Vector(w)
        else:
            raise TypeError
        
    def __sub__(self, x):
        self.Log("%s.__sub__(%s)" % (self.v,x))
        if type(x) == Vector:
            w = self.v[:]
            for i in range(0,len(self)):
                w[i] -= x[i]
            return Vector(w)
        else:
            raise TypeError
        
    def __mul__(self, x):
        self.Log("%s.__mul__(%s)" % (self.v,x))
        return self.dot(x)

    def dot(self,x):
        self.Log("%s.dot(%s)" % (self.v,x))
        if type(x) == Vector:
            w = 0.0
            for i in range(0,len(self)):
                w += self.v[i] * x[i]
            return Vector(w)
        else:
            raise TypeError
        
    def cross(self,x):
        self.Log("%s.cross(%s)" % (self.v,x))
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
    
    def Log(self,s):
        print "executing %s" % s
        