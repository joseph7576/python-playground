# from programiz

'''
In Python, a generator is a function that returns an iterator that produces a sequence of values when iterated over.
'''

'''
The yield keyword is used to produce a value from the generator and pause the generator function's execution until the next value is requested.
'''

def test_gen(n):
    val = 0
    while val < n:
        print('before yield')
        yield val # the code will pause here until next function execution
        print('after yield')
        
        val += 1
        

test_geen = test_gen(5)

print(next(test_geen))
# print(next(test_geen))
# for vo in test_geen:
#     print(vo)

#? Generator Expression Syntax -> (expression for item in iterable)

'''
A normal function to return a sequence will create the entire sequence in memory before returning the result. 
This is an overkill, if the number of items in the sequence is very large.
'''

# pipelining generators :D

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums): # underscore means we does not care about the incrementation variable over loop 
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))