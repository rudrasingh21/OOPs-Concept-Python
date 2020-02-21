#0.041 Project Solution - Transection Codes & Confirmation Code

#Adding a class level variable for Transection COdes and COnfirmation Code.

'''
As I mentioned earlier the code should contain:
- the transaction code
- the account number
- the date / time in UTC of the transaction
- the transaction number

Something like:
```D-140568-20190115154500-124```
'''

import itertools
import numbers
from datetime import timedelta
from datetime import datetime


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

'''
def generate_confirmation_code(account_number, transection_id, transection_code):
    dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    return f'{transection_code}-{account_number}-{dt_str}-{transection_id}'

'''
class Account:
    transaction_counter = itertools.count(100)
    #Adding Interst Rate
    _Interst_rate = 0.5

    #Adding Transection Code
    _transection_codes = {'deposit':'D','withdraw':'W','Interext':'I','Rejected':'X'}

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

    #class method to get Interest rate
    @classmethod
    def get_interest_rate(cls):
        return cls._Interst_rate

    #class method to set Interest rate
    @classmethod
    def set_interest_rate(cls, value):
        # if isinstance(value, numbers.Real):
        #     raise ValueError("Interest Rate Must be a Real Number")

        if value < 0:
            raise ValueError("Interest Rate can not be -ve")
        cls._Interst_rate = value

    #generate confirmation code
    #this will be like a instance method
    #because it will be an instance method , so first arg will be self
    #we can pass account_number from instance , so removing account_number
    # we have a transection counter, so we can get transection id from that counter.

    def generate_confirmation_code(self, transection_code):
        dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f'{transection_code}-{self._account_number}-{dt_str}-{next(Account.transaction_counter)}'

    #removing @staticmethod and going to use instance method
    def validate_and_set_name(self,attr_name, value, field_title):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty.')
        setattr(self, attr_name, value)

    def make_transection(self):
        return self.generate_confirmation_code('dummy')


a = Account('A100','Eric','Idle')

print(a.make_transection())
#dummy-A100-20200221141211-100

a2 = Account('A200','John','Working')
print(a2.make_transection())
#dummy-A200-20200221141314-101

