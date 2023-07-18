import functools
import time


'''
In Python, a decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function.

The outer function is called the decorator, which takes the original function as an argument and returns a modified version of it.

In fact, any object which implements the special __call__() method is termed callable. So, in the most basic sense, a decorator is a callable that returns a callable.
'''


def exe_time(func):
    def wrapper():
        start_time = time.time()
        func()
        result_time = time.time() - start_time
        print(f'-> Function:{func.__name__} ran for {round(result_time,2)} seconds.')
    
    return wrapper


# @exe_time
# def say_hello():
#     print('Heeeeloooooo')
    
# say_hello()

@exe_time
def some_heavy_stuff():
    zarb = 1
    for i in range(1,99999999):
        zarb += i
    return zarb

some_heavy_stuff()


# closure - and we have closure dunder
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 3
times3 = make_multiplier_of(3) # times3 is a closure function

# Multiplier of 5
times5 = make_multiplier_of(5) # like this - the parameter here is n
 
# Output: 27
print(times3(9)) # the parametere here is x

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))