#0.026 Delete Property

# Deleting Property from Class.

class Circle:
    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, value):
        self._color = value

    #when del_color method will invoked , it will remove the _color attribute
    #from the instance namespace (dictionary)
    def del_color(self):
        del self._color

    color = property(get_color, set_color, del_color)

c = Circle('yellow')

print(c.__dict__)
#{'_color': 'yellow'}

del c.color

print(c.__dict__)

'''
Above you can see del c.color removed _color from namespace
'''
#*************************Program Using Decorator syntax*************************

class UnitCircle:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @color.deleter
    def color(self):
        del self._color

c1 = UnitCircle('red')

print(c1.__dict__)
#{'_color': 'red'}

del c1.color

print(c1.__dict__)
#{}

#c1.color
#AttributeError: 'UnitCircle' object has no attribute '_color'

'''
AttributeError: 'UnitCircle' object has no attribute '_color'

because color is trying to access _color attribute and _color is not in dictionary.
'''

'''
NOTE:-

But Property still exist , we can redefine it.
'''

c1.color = 'blue'

'''
color is an attribute of class , it's a property type.

so it will run setter
'''

print(c1.__dict__)
#{'_color': 'red'}