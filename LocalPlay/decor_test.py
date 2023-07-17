import functools
import time

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

