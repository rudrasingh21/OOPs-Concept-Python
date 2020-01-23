#********Setting Attribute in Class*******

class MyClass:
    language = 'python'
    version = '3.6'

print(MyClass.version)          #Output:- 3.6

#setattr function

setattr(MyClass,'version','4.2')

print(MyClass.version)          #Output:- 4.2

print(getattr(MyClass, 'version')) #Output:- 4.2

#We can use dot notation too

MyClass.version = 5.2

print(MyClass.version)          #Output:- 5.2

print(getattr(MyClass, 'version')) #Output:- 5.2

#**********To define a new attribute in our class

setattr(MyClass, 'x', 100)

#OR

MyClass.y = 200

print(MyClass.x)

print(MyClass.y)