#**********Function Attribute Coding Example****************

class person:
    def say_hello():
        print('Hello')

print(person.say_hello)
#It tells that it is a function
#<function person.say_hello at 0x0000013C62632D90>

print(type(person.say_hello))
#<class 'function'>

'''
Using code
class person:
    def say_hello():        
        print('Hello')
'''
person.say_hello()
#Hello

#Now create new object OR instance
p = person()

#It is an object , which is not same as the class
print(hex(id(p)))
#0x1a474a1e860

#Access class / Function attribute via Instance
print(p.say_hello)
#Output:- is not a function now , its a bound method
#<bound method person.say_hello of <__main__.person object at 0x00000218E5D7E860>>

print(type(p.say_hello))
#Output:- now tyoe is not a function , its method now
#<class 'method'>

print(type(p.say_hello) is type(person.say_hello))
#Output:- False
#Because both objects are not same.

p.say_hello()
'''
TypeError: say_hello() takes 0 positional arguments but 1 was given

Because:- 

say_hello is a method that bound to object SO , python essentially 
injects the object p which we are using as instance as an argument to the say hello function .
'''