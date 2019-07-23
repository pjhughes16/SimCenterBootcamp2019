from printing import *
from calcs import dot

if __name__ == '__main__':
    a = [1.,2.,3.]
    b = [4.,5.,6.]
    c = dot(a,b)
    vectorprint(a)
    vectorprint(b)
    scalarprint(c)

