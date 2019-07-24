'''
Created on Oct 13, 2015

@author: pmackenz
'''

class Animal (object):
    def __init__(self, name='unknown'):
        self.name = name
        
    def sound(self):
        print("%s is silent" % self.name )
        
    def specialty(self):
        print("*** method not implemented ***")
        
    def setname(self,newname):
        self.name = newname
       
        
class Cat (Animal):
    def sound(self):
        print("%s is meowing" % self.name )


class Dog (Animal):
    def sound(self):
        print("%s is barking" % self.name )

class ServiceDog(Dog):
    def specialty(self):
        print("I am helping the blind.")