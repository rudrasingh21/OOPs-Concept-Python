#Function Attribute - Methods

class Person:
    def hello(self):
        pass

p = Person()

print(p.hello.__self__)             #returns p only.
#<__main__.Person object at 0x000001F73107E6D8>

print(p.hello.__func__)             #return function
#<function Person.hello at 0x00000159895C2D90>

'''
Methods:-
Methods are objects that combine:
1) Instance of some class
2) Function

Like any objects It has a attribute.
__self__ :- the instance the method is bound to.
__func__ :- the original function (defined in class).

'''