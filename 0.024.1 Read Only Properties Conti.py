#0.024.1 Read Only Properties Conti

#Caching Computed Property
'''
Using Property setters is sometimes useful for controlling how other
computed properties are cached.
'''

'''
In Our Last program:-

Circle :- is a class

    -->area :- is a computed property
    -->lazy computation :- only calculate area if requested.
    So if we save the value , it will save computation time in case of re- requested.
    -->cache value :- so if requested , we save the computation.
'''

'''
In case of someone change the radius,

We must have to know about it , and recalculate the area.

need to able to invalidate the cache 
'''

'''
SO , 

Control setting the radius , using a property.
    --> So we are aware , when the property has been changed.
'''
import math

class Circle:
    def __init__(self , r):
        #private attribute _r to store radius.
        self._r = r
        #private attribute area to cache the area .
        #currently it is set to None.
        self._area = None

    #getter
    @property
    def radius(self):
        return self._r

    #setter
    @radius.setter
    def radius(self, r):
        if r < 0:
            raise ValueError('Radius must be non negative')
        self._r = r
        self._area = None       #Invalidate Cache

    #Create a read only property for the area.
    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * ( self.radius ** 2 )
        return self._area


P = Circle(2)

print(P.area)
#12.566370614359172

