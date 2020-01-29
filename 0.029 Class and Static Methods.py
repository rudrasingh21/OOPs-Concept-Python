#0.029 Class and static Methods.

class MyClass:
    def hello(self):
        return 'hello'

print(MyClass.hello)
#<function MyClass.hello at 0x0000018D73982D90>

#print(MyClass.hello())
#TypeError: hello() missing 1 required positional argument: 'self'

m = MyClass()

print(m.hello)  #Function hellow bound to instance, so it's Instance method now.
#INstance method ---> Method bound to object
#<bound method MyClass.hello of <__main__.MyClass object at 0x0000020992ECF860>>
print(m.hello())

#hello

'''
So When we define a function in class,

How we call , it will alter behaviour.
'''

##******************Creating a function in a class that is always bound to class.********

'''
MyClass.fn --> Method bound to MyClass

m.fn --> this will also bound to my class (not bound to instance)

USE @classmethod decorator.
'''