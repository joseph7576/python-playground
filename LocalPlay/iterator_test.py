test_list = [1,2,3,4,5]

test_iter = iter(test_list)

# print(next(test_iter))
# print(next(test_iter))
# print(next(test_iter))

'''
__iter__() returns the iterator object itself. If required, some initialization can be performed.

__next__() must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise StopIteration.
'''

class TestIterClassPowThree:
    def __init__(self, _max=0) -> None: # you can also skip the constructor
        self.max = _max
        
    def __iter__(self):
        self.number = 0 # initialize the number - sequence
        return self
    
    def __next__(self):
        if self.number <= self.max:
            result = self.number ** 3 # number power of three
            self.number += 1
            return result
        raise StopIteration # should raise this for iterators
    

test_iter_class = TestIterClassPowThree(10)
numberOfThree = iter(test_iter_class)

for i in numberOfThree:
    print(i)
    # print(next(numberOfThree)) #? jesus -> don't do this man!
    

# Infinite Iterator :D
class InfiniteDot:
    def __iter__(self):
        return self
    
    def __next__(self):
        return '.'


# test_class = InfiniteDot()
test_dot_print = iter(InfiniteDot())

# for dot in test_dot_print:
#     print(dot, end='')
   
    
    
    
