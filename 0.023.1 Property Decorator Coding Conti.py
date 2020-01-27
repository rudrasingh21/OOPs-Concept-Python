
#Continue...  Property Decorator Coding

# Refining last code 0.023

def my_decorator(fn):
    print('decorating function')
    def inner(*args, **kwargs):
        print("running decorated function")
        result = fn(*args, **kwargs)
        return result
    return inner

@my_decorator
#Above @mydecorator is same as my_func = my_decorator(my_func)
def my_func(a, b):
    print('running undecorated function')
    return print(a + b)

'''
Output:-
decorating function
'''

my_func(1,2)

'''
Output:-
running decorated function
running undecorated function
3
'''