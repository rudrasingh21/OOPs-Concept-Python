#********Deleting Attribute in Class*******

class MyClass:
    language = 'python'
    version = '3.6'

print(MyClass.version)          #Output:- 3.6


#*******delattr

delattr(MyClass, 'version')

print(MyClass.version)          #Output:- Exception



