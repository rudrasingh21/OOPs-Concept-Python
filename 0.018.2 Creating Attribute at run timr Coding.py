
#Creating Attribute at run time

class Person:
    pass

p1 = Person()
p2 = Person()

p1.name = 'Alex'

print(p1.__dict__)
#{'name': 'Alex'}

print(p2.__dict__)
#{}

p1.say_hello = lambda :'Hello!'

print(p1.say_hello)
#<function <lambda> at 0x000001CD22E1D378>
print(p1.__dict__)
#{'name': 'Alex', 'say_hello': <function <lambda> at 0x000001CD22E1D378>}

'''
Question :-
Can we create a method on a specific Instance
So from above if we want above say_hello function 
Actually be a method , So that when we call p1.say_hello
SO then it can bind function (Eg- say_hello) to the instance p1

Answer:- Yes
Using MethodType
'''
