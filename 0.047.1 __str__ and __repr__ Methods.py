#****************************
#Polymorphism and Special Methods
#****************************

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

my_car = Car('red', 6765)

print(my_car)
#<__main__.Car object at 0x000001BE085D9E48>

print(type(my_car))
#<class '__main__.Car'>

#****************************************************
# Now use __str__
# Convert the object into string

class Car_with_dunder_str:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return 'a {self.color} car'. format(self=self)

my_car_dunder_str = Car_with_dunder_str('red', 6765)

print(my_car_dunder_str)
#a red car

print(type(my_car_dunder_str))
#<class '__main__.Car_with_dunder_str'>

print(str(my_car_dunder_str))
#a red car

#****************************************************
# Now use __repr__

class Car_repr:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '__repr__ for Car_repr'

    def __str__(self):
        return '__str__ for Car_repr'

my_car_repr = Car_repr('red', 8888)

print("I am in __repr__")

print(my_car_repr)
#__str__ for Car_repr

print(str(my_car_repr))
#__str__ for Car_repr

print(repr(my_car_repr))

#*******************Difference*****************

#__str__  ==> Easy to raed. For human consumption.

#__repr__ ==> Unambiguous

# default implementation of __str__ calls __repr__ internally

#*******************************
print('\n Difference \n')

import datetime
today = datetime.date.today()

print(datetime.date(2020, 4, 12))
#2020-04-12

print(today)
#2020-04-12

print(str(today))
#2020-04-12

print(repr(today))
#datetime.date(2020, 4, 12)

#************************* Implementation***********************

class Car_Real_imple:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '{self.__class__.__name__}({self.color}, {self.mileage})'.format(self=self)

my_Real_imple = Car_Real_imple('Red', 6666)

print(my_Real_imple)
#Car_Real_imple(Red, 6666)

print(repr(my_Real_imple))

print(str(my_Real_imple))