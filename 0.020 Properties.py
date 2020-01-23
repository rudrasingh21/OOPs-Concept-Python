#Properties:-
#We can use Property class to define properties in a class.

#Use Bare attributes
'''
class MyClass:
    def __init__(self, language):
        self.language = language

m = MyClass('Python')
print(m.language)
m.language = 'Java'
print(m.language)

#Python
#Java
'''

#Now Use Property Object for the same

# property object is a class
# Parameters:- fget , fset , fdel

'''
In general :- We start with plain attribute , and later we need to change to a property,
              we can easily do so using the property class.
              without changing the interface.

_language:- sudo private variable
'''


class MyClass:
    def __init__(self, language):
        self._language = language

    def get_language(self):
        return self._language

    def set_language(self, value):
        self._language = value

    #creating attribute on the class.
    #This attribute is an Instance of Property object
    language = property(fget=get_language, fset=set_language)

m = MyClass('Python')
print(m.language)
#Python
print(m.__dict__)
#{'_language': 'Python'}
m.language = 'Java'
print(m.language)

# Python
# Java
