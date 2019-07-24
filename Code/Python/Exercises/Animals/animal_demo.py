'''
Created on Oct 13, 2015

@author: pmackenz
'''

from animals import *

a = Animal('Hans')
b = Cat('Cleo')
c = Dog('Foster')
d = ServiceDog('Lassie')

a.sound()
b.sound()
c.sound()
d.sound()
b.specialty()
d.specialty()

a.sound()
a.setname('Baily')
a.sound()
