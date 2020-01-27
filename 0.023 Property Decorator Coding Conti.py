
#Continue...  Property Decorator Coding

# Refining last code 0.022...

def my_decorator(fn):
    print('decorating function')
    def inner(*args, **kwargs):
        print("running decorated function")
        result = fn(*args, **kwargs)
        return result
    return inner

def undecorated_function(a, b):
    print('running undecorated function')
    return print(a + b)

'''
In last code 0.022
Insted of using decorated_func (a new variable)
We can reassign it to undecorated_function
'''

undecorated_function = my_decorator(undecorated_function)

print(undecorated_function)
#decorating function
#<function my_decorator.<locals>.inner at 0x0000022D2C532EA0>


'''
Above :- What we have done is 
Using undecorated_function = my_decorator(undecorated_function)
We replaced undecorated_function
with to a decorated function 

As you can see the output of 
print(undecorated_function)
#decorating function
#<function my_decorator.<locals>.inner at 0x0000022D2C532EA0>
'''

