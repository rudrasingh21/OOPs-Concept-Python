# Creating Attributr at Run time

#Instance and setting Function attribute at run time.

#We saw that we can add instance namespace directly at run time.

class MyClass:
    language = 'Python'

obj = MyClass()

print(obj.__dict__)
#Empty
#{}

#Adding attribute to the object

obj.version = 3.7
print(obj.__dict__)
#{'version': 3.7}

#**********Creating New attribute whose value is a FUNCTION

obj.say_hello = lambda: "hello world!"       #created using lambda

print(type(obj.say_hello))

'''
Above:-
<class 'function'>

It is a function now , not a bound method.

So Bound Method is being created for us automatically when we use a 
def inside a class itself.

Because we did it later , outside the class definition 
So python will understand it like :- 
you are assigning a function to a attribute in the object. 
'''

print(obj.say_hello())
#hello world!