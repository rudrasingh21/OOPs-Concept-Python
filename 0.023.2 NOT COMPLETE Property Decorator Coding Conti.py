#Continue...  Property Decorator Coding

# Refining last code 0.023.1

'''
When you create the Property , it returns the property.
So it works like a decorator.

Property takes a function.
'''

class Person:
    def __init__(self, name):
        self._name = name

    def name(self):
        print("Getter Called")
        return self._name

p = Person('John')

print(p)
#<__main__.Person object at 0x000001F5FD107940>

print(p.name)
#<bound method Person.name of <__main__.Person object at 0x000001A5328DF6A0>>
print(type(p.name))
#<class 'method'>

print(type(p.name()))
#<class 'str'>

print(p.name())
# Getter Called
# John

#*********************OTHER WAY*********************
print('\nOther Way\n')

class Person1:
    def __init__(self, name):
        self._name = name

    def name(self):
        print('Getter Called')
        return self._name

    name = property(name)

p1 = Person1('Rudra')
print(p1)
# <__main__.Person1 object at 0x0000022D65B27D30>
print(type(p1))
# <class '__main__.Person1'>

print(p1.name)
# Getter Called
# Rudra




