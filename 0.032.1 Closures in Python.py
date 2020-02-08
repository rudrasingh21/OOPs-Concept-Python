#0.032.1 Clouseres in Python

'''
Nonlocal variable in a nested function
Before getting into what a closure is, we have to first understand what a
nested function and nonlocal variable is.

A function defined inside another function is called a nested function.
Nested functions can access variables of the enclosing scope.

In Python, these non-local variables are read only by default and we must
declare them explicitly as non-local (using nonlocal keyword) in order to modify them.

Following is an example of a nested function accessing a non-local variable.

'''

def print_msg(msg):
# This is the outer enclosing function

    def printer():
    # This is the nested function
        print(msg)

    printer()

print_msg("Hello")

'''
We can see that the nested function printer() was able to access the non-local variable 
msg of the enclosing function.
'''


# Python program to illustrate
# closures
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    return innerFunction # Note we are returning function WITHOUT parenthesis


myFunction = outerFunction('Hey!')
myFunction()

'''
As observed from above code, closures help to invoke function outside their scope.
The function innerFunction has its scope only inside the outerFunction. 
But with the use of closures we can easily extend its scope to invoke a function 
outside its scope.
'''

'''
*******************NOTE********************
When and why to use Closures:

1) As closures are used as callback functions, they provide some sort of data hiding. 
    This helps us to reduce the use of global variables.
2) When we have few functions in our code, closures prove to be efficient way. 
    But if we need to have many functions, then go for class (OOP).
'''