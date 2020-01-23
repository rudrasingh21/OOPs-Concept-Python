#Mutating Namespace of Instance

class Program:
    language = 'Python'

p = Program()

print(p.__dict__)
#{}

#change thae value of this namespace dictionary
p.__dict__['version'] = 3.7

print(p.__dict__)
#{'version': 3.7}

#now it is an attribute of object p.

print(p.version)
#3.7

print(getattr(p, 'version'))
#3.7

'''
we usually use below approach to set attribute of an object 
p.version = 3.7 
'''