#Property Coding

# class Person:
#     def __init__(self, name):
#         self.name = name
#
# p = Person('Alex')
#
# print(p.__dict__)
# #{'name': 'Alex'}
#
# #using this we can set any value:-
#
# p.name = 100
# print(p.__dict__)

'''
TO avoid this and make more control on it , we use Property.

In Python everything is public , not private like any other language.

but we use nomenclature Eg:- _name
'''

class Person:
    def __init__(self, name):
        #self._name = name
        #OR
        self.set_name(name)     #to apply same level of validation for which we created a function(bound method)

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self.name = value.strip()

        else:
            raise ValueError('Must be a non empty string')
'''
p = Person('Alex')

try:
    p.set_name(100)
except ValueError as e:
    print(e)
    
#Output:-Must be a non empty string
'''

'''
try:
    Person('')
except ValueError as e:
    print(e)

#Output:-Must be a non empty string
'''

'''
try:
    Person(100)
except ValueError as e:
    print(e)

#Output:-Must be a non empty string
'''

p = Person('Alex')
try:
    p.get_name()
except ValueError as e:
    print(e)
