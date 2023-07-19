# from: official doc and multiple sources

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# nested list comprehension
matrix_list = [[row[i] for row in matrix] for i in range(4)]

# it's the same as code below
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

# and this :D
zip_usage_on_list_like_that = list(zip(*matrix))

string = 'string'
list_string = list(string)
print(list_string)

print(chr(65)) # A

'''
Iterable -> sequence of data
Iterator -> it's protocol that has __iter__ and __next__
'''


# has attr to check if the object has that attribute
print(hasattr(str,'__iter__'))

# generator is easier iterator protocol with yield function
'''
In a function with a yield statement the state of the function is “saved” from the last call and can be picked up the next time you call a generator function.
it pause the execution on yield line and save the state ( variables ) on that function
'''

# Python code to illustrate generator expression
generator = (num ** 2 for num in range(10))
for num in generator:
    print(num)