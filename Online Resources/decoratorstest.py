'''
First-class citizen

In a given programming language design, a first-class citizen is an entity which supports all the operations generally available to other entities.
These operations typically include being passed as an argument, returned from a function, and assigned to a variable.

'''

'''
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
Decorators are usually called before the definition of a function you want to decorate. 
In this tutorial, we'll show the reader how they can use decorators in their Python functions.
'''

def plus_one(number):
    return number + 1

add_one = plus_one # assigne fundtion to variable
add_one(5)


'''
Python allows a nested function to access the outer scope of the enclosing function.
This is a critical concept in decorators -- this pattern is known as a Closure.
'''
def print_message(message):
    "Enclosong Function"
    def message_sender():
        "Nested Function"
        print(message)

    message_sender()

print_message("Some random message")



def uppercase_decorator_one(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


def say_hi():
    return 'hello there'

decorate = uppercase_decorator_one(say_hi)
decorate()

''' above function call is as the same as below

@uppercase_decorator
def say_hi():
    return 'hello there'

say_hi()
'''

import functools

# @functools.wraps(blah) -> this decorator copies the lost metadata from undecorated function to the deecorated closure

def uppercase_decorator(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper


'''Decorator Usage

- Authorization in Python frameworks such as Flask and Django
- Logging
- Measuring execution time
- Synchronization
'''



def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

function_with_no_argument()



def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3) :
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,decorator_arg3,
                          function_arg1, function_arg2,function_arg3))
            return func(function_arg1, function_arg2,function_arg3)

        return wrapper

    return decorator

pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_function_with_arguments(pandas, "Science", "Tools")