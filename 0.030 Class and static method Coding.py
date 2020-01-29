#0.030 Class and Static Method Coding

class Person:
    def hello(args='default'):
        print(f'Hello, with args = {args}')

Person.hello()
#Hello, with args = default

Person.hello(100)
#Hello, with args = 100

'''
So calling a functino from a class is just calling a function
'''



#************Create Instance**********

p = Person()

p.hello()
#Hello, with args = <__main__.Person object at 0x0000022BBEF47AC8>
#SO arg passing into hello function is an object, it is object p
#So It is behaving as a bound method , and bound to instance.

'''
#**************Classmethods*************

Sometimes we define a function in the class ,

Which don't interact with the instance.

But may be it would need to interact with class.

In that case we don't want instance to be passed to the function.
(no matter whether it is called from a class OR it is called from an Instance)

We want class to be passed as first argument of that function/method.

'''

class MyClass1:
    def hello():            #without self
        print('hello....')

    def instance_hello(self):
        print(f'hello from {self}')

    @classmethod
    def class_hello(self):
        print(f'hello from {self}')

    @staticmethod
    def static_hello():
        print('static method called...')

m = MyClass1()

MyClass1.hello()
#hello

#m.hello()
#TypeError: hello() takes 0 positional arguments but 1 was given

#above is default behaviour for the functions which are defined inside the class.

print(m.instance_hello)
#<bound method MyClass1.instance_hello of <__main__.MyClass1 object at 0x0000024BD8E07E10>>
#bound method

m.instance_hello()
#hello from <__main__.MyClass1 object at 0x00000240041A7E10>
#above :-  MyClass1 object (an instance of MyClass)

m.class_hello()
#hello from <class '__main__.MyClass1'>

MyClass1.class_hello()
#hello from <class '__main__.MyClass1'>

print(MyClass1.hello)
#<function MyClass1.hello at 0x000001F120322EA0>
#Regular FUnction

print(MyClass1.instance_hello)
#<function MyClass1.instance_hello at 0x000001F12032D268>
#Regular function

'''
Above :-

calling from instance and calling from a class receives:-

m.class_hello()
#hello from <class '__main__.MyClass1'>

MyClass1.class_hello()
#hello from <class '__main__.MyClass1'>

Same.
'''

#Calling static Method

print(MyClass1.static_hello)
#<function MyClass1.static_hello at 0x000001CECD0FD378>
#you can see it is a function , not a method

MyClass1.static_hello()
#static method called...

print(m.static_hello)
#<function MyClass1.static_hello at 0x0000014AF2DCD378>
#We called from instance , still it remains a function (and important is, not bound)

m.static_hello()
#static method called...

