#0.037 Project Creating Transection Numbers Solution:-

class TransectionID:
    def __init__(self, start_id):
        self._start_id = start_id

    def next_method(self):
        self._start_id += 1
        return self._start_id

class Account:
    transection_counter = TransectionID(100)

    def make_transection(self):
        new_trans_id = Account.transection_counter.next_method()
        return new_trans_id

#Create Two Accounts

a1 = Account()

a2 = Account()

print(a1.make_transection())
print(a2.make_transection())

print(a1.make_transection())

'''
Above Program is absolutely Correct , 
But we dont need to solve this problem using class.
We have some other way to solve this .

Using Iterators :- Given Below
'''

'''***********Using Iterators Solving Problem***********'''

def Iterator_Transection_id(start_id):
    while True:
        start_id += 1
        yield start_id

t = Iterator_Transection_id(100)

# print(t)
# print(next(t))
# print(next(t))
#
'''
<generator object Iterator_Transection_id at 0x00000154BDD65C50>
101
102
'''

'''***********Using above approach (ITERATOR) in actual Code***********'''


class Other_Way_Account:
    transection_c = Iterator_Transection_id(100)

    def other_make_transection(self):
        new_trans_id = next(Other_Way_Account.transection_c)
        return new_trans_id

#Create Two Accounts

A = Other_Way_Account()

B = Other_Way_Account()

print(A.other_make_transection())
print(B.other_make_transection())

print(A.other_make_transection())

'''***********Solving Above Problem Using Itertool***********'''

import itertools
class itertools_Way_Account:
    transection_c = itertools.count(300)

    def itertools_make_transection(self):
        new_trans_id = next(itertools_Way_Account.transection_c)
        return new_trans_id

#Create Two Accounts

I = itertools_Way_Account()

J = itertools_Way_Account()

print(I.itertools_make_transection())
print(J.itertools_make_transection())

print(I.itertools_make_transection())

'''
output:-
300
301
302
'''

#other workway:- refresh memory ,  stepsize etc.

print(help(itertools))