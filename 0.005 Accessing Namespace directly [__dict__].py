#********Accessing Attribute in Class*******

class MyClass:
    language = 'python'
    version = '3.6'

print(MyClass.version)          #Output:- 3.6

print(MyClass.__dict__['language']) #Output:- python

print(MyClass.__dict__.keys())
#Output:- dict_keys(['__module__', 'language', 'version', '__dict__', '__weakref__', '__doc__'])

print(MyClass.__dict__.values())
#Output:- dict_values(['__main__', 'python', '3.6', <attribute '__dict__' of 'MyClass' objects>, <attribute '__weakref__' of 'MyClass' objects>, None])

print(list(MyClass.__dict__.items()))
#[('__module__', '__main__'), ('language', 'python'), ('version', '3.6'), ('__dict__', <attribute '__dict__' of 'MyClass' objects>), ('__weakref__', <attribute '__weakref__' of 'MyClass' objects>), ('__doc__', None)]
