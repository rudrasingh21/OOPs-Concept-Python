

#MyClass is a CLASS
#language is a DATA ATTRIBUTE
class MyClass:
    language = 'Python'

#my_obj is INSTANCE of MyClass
my_obj = MyClass()

#MyClass has it's own namespace , it has it's dictionary
print(MyClass.__dict__)
#'language': 'Python'

#my_obj has it's own namespace , it has it's own dictionary
print(my_obj.__dict__)
#{}

print(MyClass.language)
#Python

#First Python start looking my_obj in MyClass namespace
#If it has it , it returns
#If its not, it looks in type(class) of my_obj, i.e. MyClass
#And it returns Python
print(my_obj.language)
#Python

