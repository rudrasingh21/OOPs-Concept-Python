#0.044 Project Solution - Transactions

#Adding a class level variable for Transaction COdes and COnfirmation Code.

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
def generate_confirmation_code(account_number, transaction_id, transaction_code):
    dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    return f'{transaction_code}-{account_number}-{dt_str}-{transaction_id}'

'''

from collections import namedtuple
confirmation = namedtuple('Confirmation','account_number, transaction_code, transaction_id, time_utc, time')

class Account:
    transaction_counter = itertools.count(100)
    #Adding Interst Rate
    _Interst_rate = 0.5

    #Adding Transaction Code
    _transaction_codes = {'deposit':'D','withdraw':'W','Interext':'I','Rejected':'X'}

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
    # we have a transaction counter, so we can get transaction id from that counter.

    def generate_confirmation_code(self, transaction_code):
        dt_str = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        return f'{transaction_code}-{self._account_number}-{dt_str}-{next(Account.transaction_counter)}'

    #removing @staticmethod and going to use instance method
    def validate_and_set_name(self,attr_name, value, field_title):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty.')
        setattr(self, attr_name, value)

    def make_transaction(self):
        return self.generate_confirmation_code('dummy')

    #We will make a static method because we don't need anything from instance sdata

    @staticmethod
    def parse_confirmation_code(confirmation_code, preferred_timezone=None):
        parts = confirmation_code.split('-')
        if len(parts) != 4:
            raise ValueError('Invalide Confirmation Code')

        #Use Unpacking
        transaction_code, account_number, raw_dt_utc, transaction_id = parts

        try:
            dt_utc = datetime.strptime(raw_dt_utc, '%Y%m%d%H%M%S')
        except ValueError as ex:
            raise ValueError('Invalid Transaction Datetime') from ex

        if preferred_timezone is None:
            preferred_timezone = TimeZone('UTC', 0, 0)

        if not isinstance(preferred_timezone, TimeZone):
            raise ValueError('Invalid TimeZOne specified.')

        dt_preferred = dt_utc + preferred_timezone.offset
        dt_preferred_str = f"{dt_preferred.strftime('%Y-%m-%d %H:%M:%S')} ({preferred_timezone.name})"

        return confirmation(account_number, transaction_code, transaction_id, dt_utc.isoformat(), dt_preferred_str)

###################################$$$$$$$$$$$$$$$$$$

    @staticmethod
    def validate_real_number(value, min_value=None):
        if not isinstance(value, numbers.Real):
            raise ValueError('Value must be a real number.')

        if min_value is not None and value < min_value:
            raise ValueError(f'Value must be at least {min_value}')

        # validation passed, return valid value
        return value
    def deposit(self, value):
        value = Account.validate_real_number(value, 1)

        #NOte:- Because we have created validate real number function so below code is not is use added validation function
        #     raise ValueError('Deposit Value must be a real Number')
        # if value <= 0:
        #     raise  ValueError('Must be a Positive Number')

        #we will check for the transaction code of deposit
        #its a class variable so we will use class name Account.
        transaction_code = Account._transaction_codes['deposit']

        #Its a instance method so call using self
        conf_code = self.generate_confirmation_code(transaction_code)

        self._balance += value
        return conf_code

    def withdraw(self, value):
        value = Account.validate_real_number(value, 1)
        accepted = False
        if self._balance - value < 0:
            #insufficient fund
            transaction_code = Account._transaction_codes['Rejected']
        else:
            accepted = True
            transaction_code = Account._transaction_codes['withdraw']

        conf_code = self.generate_confirmation_code(transaction_code)

        if accepted:
            self._balance -= value

        return conf_code

    def pay_interest(self):
        interest = self.balance * Account.get_interest_rate() / 100
        conf_code = self.generate_confirmation_code(self._transaction_codes['interest'])
        self._balance += interest
        return conf_code

a = Account('A100', 'Eric', 'Idle', initial_balance=100)

try:
    a.deposit(-100)
except ValueError as ex:
    print(ex)
#Must be a Positive Number

print(a.deposit(100))
#D-A100-20200221190851-100

print(a.balance)
#200.0

print(a.withdraw(150))
#W-A100-20200221191008-101

print(a.balance)
#50.0


try:
    a.withdraw(-100)
except ValueError as ex:
    print(ex)
#Value must be at least 1

print(a.withdraw(100))
#X-A100-20200221192225-102