
'''
Question :-
Can we create a method on a specific Instance
So from above if we want above say_hello function
Actually be a method , So that when we call p1.say_hello
SO then it can bind function (Eg- say_hello) to the instance p1

Answer:- Yes
Using MethodType
'''

from types import MethodType
class Person:
    def __init__(self, name):
        self.person_name = name

p1 = Person('Eric')
p2 = Person('Alex')

#Above 2 object , and each has there own state.

print(p1.__dict__)
print(p2.__dict__)
#{'person_name': 'Eric'}
#{'person_name': 'Alex'}

#Now create a method object
#for that create a function

def say_hello(self):
    return f'{self.person_name} says Hello'

print(type(say_hello))
#<class 'function'>

#Now in this function we have to pass an object which has person_name property
print(say_hello(p1))
#Eric says Hello

print(say_hello(p2))
#Alex says Hello

'''
Add this function as a method to my instance.

or creating bound method:- check below
'''

p1_say_hello_bound_method = MethodType(say_hello,p1)

print(p1_say_hello_bound_method)
#<bound method say_hello of <__main__.Person object at 0x0000025CA3D569B0>>
print(p1.__dict__)
#{'person_name': 'Eric'}

print(p2.__dict__)
#{'person_name': 'Alex'}

#NOTE:- As you can see , This Bound Method is not in p1 or p2's namespace

#setting attribute:-

p1.say_hello= p1_say_hello_bound_method

print(p1.__dict__)
#{'person_name': 'Eric', 'say_hello': <bound method say_hello_new of <__main__.Person_New object at 0x000001EC47197E48>>}

print(hex(id(p1)))
#0x168eae97e48

print(p1.say_hello())
#Eric says Hello

#OR

getattr(p1, 'say_hello')()
#Eric says Hello