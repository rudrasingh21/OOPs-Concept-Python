#The State of a class is stored in a dictonary.

#All attribte name is string

class MyClass:
    pass

#it creates MyClass object

print(type(MyClass)) #Output:- type object

#Automatially provides certain attribute(state) and methods (behavior)

#So certain attributes are already there by Python
#Eg:- [STATE]

print(MyClass.__name__)  #Output:- MyClass --> It is actually a string  [STATE]

#Eg:- [BEHAVIOR]

MyClass()           #We are calling it .
                    #When we call it Python return an Instance of that perticullar type.

print(type(MyClass))

a = MyClass()
#a is instance of class test.

print(type(a))

print(isinstance(a, MyClass))


######**************************

print(type(MyClass))
print(MyClass.__dict__)


#Above shows that class MyClass stores everything in dictonary
#and everything is string inside it .
#Eg:- {'__module__': '__main__',...}