#0.041 Project Solution - Account Balance

#Interest Rate

import itertools
import numbers
from datetime import timedelta


class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes):
        if name is None or len(str(name).strip()) == 0:
            raise ValueError('Timezone name cannot be empty.')

        self._name = str(name).strip()
        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError('Hour offset must be an integer.')

        if not isinstance(offset_minutes, numbers.Integral):
            raise ValueError('Minutes offset must be an integer.')

        if offset_minutes < -59 or offset_minutes > 59:
            raise ValueError('Minutes offset must between -59 and 59 (inclusive).')

        offset = timedelta(hours=offset_hours, minutes=offset_minutes)

        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError('Offset must be between -12:00 and +14:00.')

        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes
        self._offset = offset

    @property
    def offset(self):
        return self._offset

    @property
    def name(self):
        return self._name

    def __eq__(self, other):
        return (isinstance(other, TimeZone) and
                self.name == other.name and
                self._offset_hours == other._offset_hours and
                self._offset_minutes == other._offset_minutes)

    def __repr__(self):
        return (f"TimeZone(name='{self.name}', "
                f"offset_hours={self._offset_hours}, "
                f"offset_minutes={self._offset_minutes})")


class Account:
    transaction_counter = itertools.count(100)
    #Adding Interst Rate
    Interst_rate = 0.5

    #Adding timezone here
    def __init__(self, account_number, first_name , last_name,
                 initial_balance=0,timezone=None):
        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name

        self._balance = float(initial_balance)

        if timezone is None:
            #if timezone is none then setting timezone using timezone instance
            timezone = TimeZone('UTC',0 , 0)
        self.timezone = timezone

    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self,value):
        self.validate_and_set_name('_first_name', value, 'First Name')

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self.validate_and_set_name('_last_name', value, 'Last_Name')

    #Read balance property
    @property
    def balance(self):
        return self._balance


    # Create timezone property
    @property
    def timezone(self):
        return self._timezone

    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError('TimeZone must be a valid timezone object.')
        self._timezone = value

    #removing @staticmethod and going to use instance method
    def validate_and_set_name(self,attr_name, value, field_title):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty.')
        setattr(self, attr_name, value)

a1 = Account('1111','Monty','Python')
a2 = Account('2222','charly','Python')

print(a1.Interst_rate)
#0.5
print(a2.Interst_rate)
#0.5

#You can access it using class as well
print(Account.Interst_rate)
#0.5

#Change the interest rate on the class:-
Account.Interst_rate=10
print(Account.Interst_rate)
#10

print(a1.Interst_rate)
#10
print(a2.Interst_rate)
#10

a1.Interst_rate = 100

print(Account.Interst_rate)
#10
print(a1.Interst_rate)
#100
print(a2.Interst_rate)
#10

print(a1.__dict__)
'''
{'_account_number': '1111', '_first_name': 'Monty', '_last_name': 'Python', 
'_balance': 0.0, '_timezone': TimeZone(name='UTC', offset_hours=0, offset_minutes=0), 
'Interst_rate': 100}
'''

'''
In above code we dont want to change the interest rate on instance level.

lets fix it in next note .
'''
