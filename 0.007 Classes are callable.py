class MyClass:
    pass

my_Obj = MyClass

print(my_Obj)
#<class '__main__.MyClass'>

my_Obj = MyClass() #Calling MyClass
print(my_Obj)

# It will create an object of MyClass
#<__main__.MyClass object at 0x0000022445CEE6D8>

print(type(MyClass))
#type of class is type
#<class 'type'>

print(type(my_Obj))
#type of my_obj is MyClass
#<class '__main__.MyClass'>

print(isinstance(my_Obj,MyClass))
#my_Obj is instance of MyClass
#True

#****************Instantiating Class
'''
When we  call a class , a class instance object is created.

This class instance object has its own NAMESPACE. 

This object has some attributes , python automatically implements to us.

__dict__ :- Object local namespace

__class__ :- tells us which class was used to instantiate the obj.

'''
#below my_Obj-[instance of class] has its own namespace
print(my_Obj.__dict__)
#{}

#below MyClass - [class] has its own namespace
print(MyClass.__dict__)

