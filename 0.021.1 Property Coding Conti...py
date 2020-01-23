#Property Coding Conti.....


class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print("getter called")
        return self._name

    def set_name(self, value):
        print("setter called")
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value.strip()
        else:
            raise ValueError('Must be a non empty string')

    def del_name(self):
        print("deleter called")
        del self._name

    name = property(fget=get_name , fset=set_name, fdel=del_name)

p = Person('Alex')

print(p.__dict__)
#{'_name': 'Alex'}

print(p.name)
#Alex

p.name = 'Rudra'
#setter called

print(p.__dict__)
#{'_name': 'Rudra'}

setattr(p, 'name', 'seema')
#setter called

print(p.__dict__)
#{'_name': 'seema'}

del p.name
#deleter called

print(p.__dict__)
#{}

print(Person.__dict__)
#{'__module__': '__main__', '__init__': <function Person.__init__ at 0x0000016C24BF2D90>,
#  'get_name': <function Person.get_name at 0x0000016C24BF2EA0>,
# 'set_name': <function Person.set_name at 0x0000016C24BFD268>,
# 'del_name': <function Person.del_name at 0x0000016C24BFD2F0>,
# 'name': <property object at 0x0000016C248D8CC8>,
# '__dict__': <attribute '__dict__' of 'Person' objects>,
# '__weakref__': <attribute '__weakref__' of 'Person' objects>,
# '__doc__': None}

print(help(Person))
'''
Help on class Person in module __main__:

class Person(builtins.object)
 |  Methods defined here:
 |  
 |  __init__(self, name)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  del_name(self)
 |  
 |  get_name(self)
 |  
 |  set_name(self, value)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  name

None
'''
