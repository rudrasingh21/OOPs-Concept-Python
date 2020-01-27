#Continue...  Property Decorator Coding

# Refining last code 0.023.3

def get_pro(self):
    return 'getter called'

def set_pro(self):
    return 'setter called'

def del_pro(self):
    return 'deleter called'

p = property(get_pro)

print(p)
#<property object at 0x000002EDEE813D18>

print(p.fget)
#<function get_pro at 0x000002EDEE9AD378>

print(p.fset)
#None

print(p.fdel)
#None

#print(p.__dict__)
#AttributeError: 'property' object has no attribute '__dict__'

print(dir(p))

p1 = p.setter(set_pro)

print(p is p1)
#False

print(p1.fget)
#<function get_pro at 0x0000027CCCBDD378>

print(p1.fset)
#<function set_pro at 0x0000020A2AF8D400>


