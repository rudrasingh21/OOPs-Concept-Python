#Function Attribute - Instance Methods
'''
 When we call a function which is inside a class ,
 But from the instance.
 It Becomes a method.
 Which is function bound to perticular instance.
 That allows us inside the function body to use the state of perticular instance , that was passed in.
'''
'''
We have to account for that extra argument , when we define functions in our 
classes - Otherwise we can not use them as methods bound to our instance.

These Functions are usually called Instance Mathods:-
'''

'''
NOTE:- Below:-
def say_hello(self):- self will receive instance object.
                      We often call this an instance method.
                      At this point it is just a regular function.
                       
'''
class MyClass:
    def say_hello(self):
        print("Hello World")

my_obj = MyClass()
my_obj.say_hello
'''
NOTE:- Now on above :- (my_obj.say_hello)it's a method. 
                        And is bound to my_obj.
                        Function say_hello is bound to object my_obj.
                        An instance of MyClass.
                       
'''

#OR
print(my_obj.say_hello)
#<bound method MyClass.say_hello of <__main__.MyClass object at 0x00000199C2547438>>

my_obj.say_hello()
#Hello World

MyClass.say_hello(my_obj)
#Hello World

'''
Functions in our class can have there own paremeter.

When we call corresponding instance method with argument --> they pass to the method as well.

And the method receives the instance object reference as the first argument..

We have access to the instance (and class) attributes.
'''

#class
class MyClass:
    #class attribute
    language = 'Python'

#Instance Mathod
    def say_hello(self, name):
        return f'Hello {name}! I am {self.language}.'

#Instance of MyClass

python = MyClass()

# using below , I am invoking or calling bound method (say_hello) method bound to python.
#As well passed extra Arg 'John'
print(python.say_hello('John'))    #in the backend-> MyClass.say_hello(python,'john')

#Hello John! I am Python.

#Another Instance of MyClass

java = MyClass()

#set property on the instance
java.language = 'Java'

#below if we call say_hello('John') on java object.
#say_hello method has been bound with java object

print(java.say_hello('John'))   #So in the backend-> MyClass.say_hello(java,'john')
