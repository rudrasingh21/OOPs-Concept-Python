#********Getting Attribute in Class*******

class MyClass:
    language = 'python'
    version = '3.6'

#MyClass is a class
#It is also an object of type type.

#*********Retrieving Attribute Values from object

#********getattr function

print(getattr(MyClass, 'language'))

print(getattr(MyClass, 'version'))

#setting default values for the attribute which doesnot exist.

print(getattr(MyClass, 'x' , 'NA'))

#*******dot notation

print(MyClass.language)