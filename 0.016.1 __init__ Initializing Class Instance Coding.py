#Initializing CLass Instance Coding:-

class Person:
    def __init__(self,name):
        self.given_name = name

p = Person("rudra")

'''
Above:-
#We are passing arg here ,like:- p = New_Person("rudra) 
#  because __init__ is defined
# SO it will take an extra value.
'''

print(hex(id(p)))
#0x217acacf6d8

print(p.__dict__)
#{'given_name': 'rudra'}

r = Person('Rudra')

print(r.__dict__)
#{'given_name': 'Rudra'}

'''
Important:- because we had __init__ method already defined.
            So as soon as we created an instance (p and r) of class.
            It automatically add it into name space of the object.
            because __init__method is already defined.
{'given_name': 'rudra'}
{'given_name': 'Rudra'}
'''

#*************WIthout __init__

class New_Person:
    def initialization(self, name):
        self.ini_name = name

p = New_Person()
'''
Above:-
#We are not passing any arg here like:- p = New_Person("rudra) 
#  because __init__ not defined
# SO it will not take any extra value.
'''
print(p.__dict__)
#its emply now , because __init__method is not define.
#So for that we have to define it.

#NOTE:-

p.initialization('Rudra')

print(p.__dict__)
#{'ini_name': 'Rudra'}

'''
NOTE:-
1) SO __init__ method takes an argument while object creation. Eg- p = New_Person('rudra')
2) insted of first creating the obj , not passing anything as initializer . eg- p = New_Person()
3) and then initialize it by calling another method , bound to the obj. eg- p.initialization('Rudra')

So point 2 and point 3 automatically taken care once we create __init__.
'''