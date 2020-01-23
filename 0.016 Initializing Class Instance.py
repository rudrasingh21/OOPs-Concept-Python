#***************Initializing Class Instance**************

class MyClass:
    language = 'Python'

obj = MyClass()

print(obj.__dict__)
#{}
#Above a namespace for the object has been created and initialized
#above it has been initialized to an empty dictonary.

'''
When we instantiate a class , by default does twi separate things:
1) create a new instance of class
2) Initialize a name space of class.
'''

'''
WE can provide a custom initializer method , so that python will use that one ,
Insted of it's own.
'''

class New_MyClass:

    #class attribute , so language is a class attribute
    language = 'Python'

    #__init__ Function is also a class attribute as it is in class namespace.

    #__init__ to initialize
    def __init__(obj, version):
        obj.lang_version = version

    #NOTICE:- __init__ function is defined to work as a bound instance method

'''
When we call :-
print(New_MyClass('3.7'))
-->python creates new instance of object with an empty name space.
-->If we have __init__ function defined in class then it calles __init__
--> as bound method to newly created object
--> obj.__init__('3.7')




print(obj.__dict__)

