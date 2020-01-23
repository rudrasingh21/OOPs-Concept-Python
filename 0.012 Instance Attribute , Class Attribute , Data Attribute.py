#Instance Attribute and Class Attribute

#Class Attribute
class MyClass:
    language = 'Python'

#Instance Attribute
my_obj = MyClass()

other_obj = MyClass()

my_obj.language = 'java'        #Instance Attribute


print(MyClass.language)
#Python
print(my_obj.language)
#java
print(other_obj.language)
#python