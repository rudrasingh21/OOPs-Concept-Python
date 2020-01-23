# Create and Bind a method to an Instance at run Time

#We can create a bind method to an instance at run time.

class MyClass:
    language = 'Python'

obj = MyClass()

from types import MethodType

print(type(MethodType))
#<class 'type'>
#So its a type class

obj.say_hello  = MethodType(lambda self: f'Hello {self.language}!', obj)

#Now say_hello is a method object bound to obj

print(obj.say_hello)
#<bound method <lambda> of <__main__.MyClass object at 0x000001BCA5AB7AC8>>

print(obj.say_hello())
#Hello Python!