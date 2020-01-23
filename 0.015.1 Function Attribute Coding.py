#**********Function Attribute Coding Example****************

class Person:
    def say_hello(*args):
        print("say_hello args: ",args)

print(Person.say_hello)
#<function Person.say_hello at 0x0000016C41662D90>

Person.say_hello()
#say_hello args:  ()

Person.say_hello("rudra")
#say_hello args:  ('rudra',)

Person.say_hello('rudra', 'seema','singh')
#say_hello args:  ('rudra', 'seema', 'singh')

#CREATE INSTANCE

p = Person()

print(hex(id(p)))
#0x15fb1ba7d68

print(p.say_hello)
#<bound method Person.say_hello of <__main__.Person object at 0x0000020DF54E7D68>>

p.say_hello()
#say_hello args:  (<__main__.Person object at 0x000002B1BC167D68>,)

'''
NOTE:- Above , you can see that python injected p as an argument inside the say hello .
        See the above output.
'''

'''
Important Advantage:- So Advantage of this is ,
                    Inside the say hello function , 
                    we have access of instance ,where it was called from.
                    in other words , we have access of state and other functionality 
                    that inside of that instance.
'''

#Check Example below:-

class NewPerson:
    def set_name(instance_obj, new_name):
        #setting new property name and assigned it variable new_name
        instance_obj.name = new_name

p = NewPerson()

p.set_name("Alex")
print(p.__dict__)
#{'name': 'Alex'}

#OR we also can do it

NewPerson.set_name(p,"RUdra")
print(p.__dict__)
#{'name': 'RUdra'}

'''
Important Note:- 
NewPerson.set_name(p,"RUdra"):-
                            We are calling function set_name at the class level,
                            and passing the instance which we want.
                            
                            So set_name function  in the class, which becomes a method , 
                            when we call it from instance, 
                            is able to access and manipulate the namespace of the object that being
                            used when the method is called.
                            
                            we basically use self in place of instance_obj

'''