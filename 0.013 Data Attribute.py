#**********Data Attribute**************

class BankAccount:
    apr = 1.2

print(BankAccount.__dict__)
#{'__module__': '__main__', 'apr': 1.2, '__dict__': <attribute '__dict__' of 'BankAccount' objects>, '__weakref__': <attribute '__weakref__' of 'BankAccount' objects>, '__doc__': None}

print(BankAccount.apr)
#1.2

#Now Create instances of class
acc_1 = BankAccount()
acc_2 = BankAccount()

#check if both instance are same
print(acc_1 is acc_2)
#False

#check for namespace dictionary
print(acc_1.__dict__)
print(acc_2.__dict__)
# {}
# {}
#NOTE:- Showing empty but still they have apr attribute.
#       Instance dictionary is empty , so it will come from class

print(acc_1.apr)
print(acc_2.apr)
#1.2
#1.2

#NOTE : -As above we can say that , we can access class attribute from instances as well.

#Adding class attribute , after class has been defined.

BankAccount.account_type = 'Savings'

print(acc_1.account_type)
print(acc_2.account_type)
# Savings
# Savings

acc_1.apr = 0

print(acc_1.apr)
#0
print(acc_2.apr)
#1.2

#As well check the name space
print(acc_1.__dict__, acc_2.__dict__)
#{'apr': 0} {}

print(acc_1.apr , acc_2.apr)
#0 1.2

#Setting attribute on an INSTANCE OR on an OBJECT
setattr(acc_2,'apr',10)

print(acc_2.__dict__)
#{'apr': 10}

print(getattr(acc_2,'apr'))
#10

acc_1.bank = 'HDFC Saving Bank'

print(acc_1.__dict__)
#{'apr': 0, 'bank': 'HDFC Saving Bank'}

print(BankAccount.__dict__)
#{'__module__': '__main__', 'apr': 1.2, '__dict__': <attribute '__dict__' of 'BankAccount' objects>,
# '__weakref__': <attribute '__weakref__' of 'BankAccount' objects>, '__doc__': None, 'account_type': 'Savings'}

print(type(BankAccount.__dict__))
#<class 'mappingproxy'>             #It is a mapping proxy

print(type(acc_1.__dict__))
#<class 'dict'>                     #It is a regualr dictonary


