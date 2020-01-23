class MyClass:
    pass

m = MyClass()

print(type(m))
#<class '__main__.MyClass'>

print(m.__class__)
#<class '__main__.MyClass'>

#NOTE:- It is possible to change dunder class property

class MyClass_New:
    __class__ = str     #redefining class attribute

new = MyClass_New()

print(new.__class__)
#<class 'str'>      #gives a wrong result 

print(type(new))
#<class '__main__.MyClass_New'>