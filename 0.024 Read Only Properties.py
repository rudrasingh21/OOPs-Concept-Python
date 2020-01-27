#0.024 Read Only Properties:-

'''
(1)
TO Create a read only property,
We just need to create a property with only the get accessor defined.
-> not truly read only since underlying storage variable could be accessed directly.

(2)
Useful for computed property
'''
import math

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

c = Circle(2)
print(type(c))
#<class '__main__.Circle'>

print(c.area)
#<bound method Circle.area of <__main__.Circle object at 0x0000018113EB7AC8>>

print(c.area())
#12.566370614359172

#************************Other Way*******************
'''
Since Area is not a method , 
It's a property of a circle 

above , you can see , print(c.area) is a method.
'''

class circle1:
    def __init__(self,r):
        self.r = r

    @property
    def area(self):
        return math.pi * self.r * self.r

c = circle1(2)

print(c)
#<__main__.circle1 object at 0x000001E0C8D007F0>

print(c.area)
#12.566370614359172

'''
c.area is a property now.
'''

