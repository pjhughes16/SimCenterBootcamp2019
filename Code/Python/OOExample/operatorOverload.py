'''
Created on Apr 30, 2009

@author: pmackenz
'''

class MyClass(object):

    def __init__(self,v, s):
        print("entering __init__({})".format(v))
        self.val = v
        self.my_name = str(s)
        
    def __len__(self):
        print("entering __len__()")
        return len(self.val)
    
    def __add__(self, y):
        print("entering __add__({})".format(y.val))
        name = "%s+%s" % (self.my_name, y.name())
        return MyClass( self.val + y.val, name )
    
    def __sub__(self, y):
        print("entering __sub__({})".format(y.val))
        name = "%s-%s" % (self.my_name, y.name())
        return MyClass( self.val - y.val, name )
    
    def name(self):
        print("entering __name__()")
        return self.my_name
    
    def setname(self, s):
        print("entering __setname__({})".format(s))
        self.my_name = s
    
    def __str__(self):
        print("entering __str__()")
        return str( self.val )
    
    
def main():
    x = MyClass( 4, 'peter')
    print("variable x = {} (type: {}, name: {})".format(x, type(x), x.name()))
    y = MyClass( 7, 'joe' )
    print("variable y = {} (type: {}, name: {})".format(y, type(y), y.name()))
    z = x + y
    print("variable z = {} (type: {}, name: {})".format(z, type(z), z.name()))
    z = y + x
    print("variable z = {} (type: {}, name: {})".format(z, type(z), z.name()))
    z.setname('paul')
    print("variable z = {} (type: {}, name: {})".format(z, type(z), z.name()))
    a = x - y
    print("variable a = {} (type: {}, name: {})".format(a, type(a), a.name()))
    b = z + x
    print("variable b = {} (type: {}, name: {})".format(b, type(b), b.name()))

# main execution 
main() 
        
        
