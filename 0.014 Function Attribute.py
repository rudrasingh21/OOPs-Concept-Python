#Function Attribute

class MyClass:
    def say_hello(self=None):
        print("Hello World!")

my_obj = MyClass()

#NOTE:- Check below - It Is a Function
print(MyClass.say_hello)
#<function MyClass.say_hello at 0x000001F350B82EA0>

#NOTE:- Check below - It is a BOUND METHOD of MyClass.sayhello
print(my_obj.say_hello)
#<bound method MyClass.say_hello of <__main__.MyClass object at 0x000001A13819E6D8>>

#Using getatter
print(getattr(my_obj, 'say_hello'))
#<bound method MyClass.say_hello of <__main__.MyClass object at 0x0000016DA8A2E6D8>>

print(getattr(MyClass, 'say_hello'))
#<function MyClass.say_hello at 0x000002AFC0E12EA0>

MyClass.say_hello()
my_obj.say_hello()

#*********************************
'''
>>> class MyClass:
...     def say_hello():
...         print("Hello World!")
...
>>> my_obj = MyClass()

>>> MyClass.say_hello
<function MyClass.say_hello at 0x000001F7A94F0268>

>>> my_obj.say_hello
<bound method MyClass.say_hello of <__main__.MyClass object at 0x000001F7A95090F0>>

>>> MyClass.say_hello()
Hello World!

>>> my_obj.say_hello()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: say_hello() takes 0 positional arguments but 1 was given

NOTE:- Please see above given error.

'''

'''
Methods:-

Method is an actual object type in Python.

Like a function , it is callable

But unlike a Function , it is bound to some object

and that object is passed to the method as its first parameter.

Example:-

my_obj.say_hello()
-> say_hello is a method object
-> It is bound to my_obj
-> say_hello function ( A method of a class ) is bound to my_obj
-> when my_obj.say_hello() is called , the bound object my_obj is injected as 
    first parameter to the method say_hello.
-> So it is doing below:-
-> MyCLass.say_hello(my_obj) [it does automatically for us when we call 'my_obj.say_hello()]

'''