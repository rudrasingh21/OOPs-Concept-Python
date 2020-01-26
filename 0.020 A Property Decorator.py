#0.020 A :- Python Property Decorator

'''
As we discussed that we can decorate a function using decorators.
There are some built-in decorators.

Python @property is one of the built-in decorators. The main purpose of any
decorator is to change your class methods or attributes in such a way so
that the user of your class no need to make any change in their code.
Consider the following class segment:
'''

class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.gotmarks = self.name + ' obtained ' + self.marks + ' marks.'

st = Students('Rudra', '55')

print(st.name)
print(st.marks)
print(st.gotmarks)

'''
Rudra
55
Rudra obtained 55 marks.
'''

'''
Now say we want to change the name attribute of the student class then what will happen?
Append the following 3 line after the previous code:
'''

st.name = "Anusha"
print(st.name)
print(st.gotmarks)

'''
Anusha
Rudra obtained 55 marks.
'''

'''
Notice that the name attribute got changed but the sentence that was created by
the gotmarks attribute remained same as it was set during the initialization of
the student object.

But we want gotmarks also to be changed when student name is updated.
Here comes the use of python property decorator.

We can solve this problem with the following code
'''

#***************Using Python Function to solve above problem*****************

class Students1:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def gotmarks1(self):
         return self.name + ' obtained ' + self.marks + ' marks'

st1 = Students1("Jaki", "25")
print(st1.name)
print(st1.marks)
print(st1.gotmarks1())

st1.name = "Anusha"
print(st1.name)
print(st1.gotmarks1())

'''
Output:-
Jaki
25
Jaki obtained 25 marks
Anusha
Anusha obtained 25 marks
'''

'''
Wow!!! Our requirement is solved. But have a close look at the code.
We have removed the gotmarks attribute from the constructor and added
a method named gotmarks.

So now in our class there is no attribute named gotmarks and we have a
method named gotmarks().

And for this change, any user who is using my class will be in trouble as
they have to replace all the attribute gotmarks with a function call gotmarks().
Assume there are 1000 lines of code then how troublesome it will be for the coder.
'''

#*******Solving above problem using Python property decorator***********

'''
So we will solve this problem in pythonic way using the python property decorator.
Notice the following code:


@property
def gotmarks(self):
   return self.name + ' obtained ' + self.marks + ' marks'
It will provide the same output as before, and don’t forget to remove the ‘()’
after gotmarks when printing it. Just writing @property above the
function gotmarks() make it available to be used as a property.

And the user of our class doesn’t even know that attribute gotmarks is removed
and we have a function for that. This is how the property decorator helps in keeping
our code loosely coupled with the client code.
'''


class Students2:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @property
    def gotmarks2(self):
         return self.name + ' obtained ' + self.marks + ' marks'

st2 = Students2("umesh", "285")
print(st2.name)
print(st2.marks)
print(st2.gotmarks2)

st2.name = "Chane"
print(st2.name)
print(st2.gotmarks2)

'''
umesh
285
umesh obtained 285 marks
Chane
Chane obtained 285 marks
'''

#************Python property setter*****************

'''
Now let’s say we want to set the name and marks attribute when we change 
the value of gotmarks. Deeply observe the code:
'''

class Student4:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @property
    def gotmarks4(self):
        return self.name + ' obtained ' + self.marks + ' marks'

    @gotmarks4.setter
    def gotmarks4(self, sentence):
        name, rand, marks = sentence.split(' ')
        self.name = name
        self.marks = marks


st4 = Student4("ninja", "2500")
print(st4.name)
print(st4.marks)
print(st4.gotmarks4)
print("##################")

st4.name = "ranjeet"
print(st4.name)
print(st4.gotmarks4)
print("##################")

st4.gotmarks4 = 'abhinav obtained 360'
print(st4.gotmarks4)
print(st4.name)
print(st4.marks)

'''
ninja
2500
ninja obtained 2500 marks
##################
ranjeet
ranjeet obtained 2500 marks
##################
abhinav obtained 360 marks
abhinav
360
'''

'''
As we want to update the value of name and marks when we are setting 
the value of gotmarks. So using the setter of @proprety decorator we can achieve this.

Notice that we have written @gotmarks.setter that means we are applying the 
setter on the gotmarks method. And then we are splitting the sentence and updating the 
value of name and marks.
'''