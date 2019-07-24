'''
Created on Oct 16, 2014

@author: pmackenz
'''
from numpy import array
import numpy as np

class Vector(object):
    '''
    vector class implementation using numpy:
    
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
    '''

    def __init__(self, v):
        '''
        Constructor
        '''
        self.v = array(v)
        
    def asarray(self):
        return self.v
        
    def __str__(self):
        return str(self.v)
    
    def __repr__(self):
        return "Vector({})".format((self.v))
    
    def __len__(self):
        return len(self.v)
    
    def __getitem__(self, i):
        return self.v[i]

    def __div__(self, x):
        raise NotImplemented
    
    def __add__(self, x):
        if type(x) == Vector:
            return Vector(self.v + x.asarray())
        else:
            raise TypeError
        
    def __sub__(self, x):
        if type(x) == Vector:
            return Vector(self.v - x.asarray())
        else:
            raise TypeError
        
    def __mul__(self, x):
        return self.dot(x)

    def dot(self,x):
        if type(x) == Vector:
            return np.dot(self.v,x.asarray())
        else:
            raise TypeError
        
    def cross(self,x):
        if type(x) == Vector:
            return Vector(np.cross(self.v,x.asarray()))
        else:
            raise TypeError
        