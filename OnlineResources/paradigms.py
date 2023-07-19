# from: https://www.geeksforgeeks.org/programming-paradigms-in-python/

'''
Aspect-oriented programming: This paradigm is based on the idea of separating cross-cutting concerns from the main functionality of a program. 
Python does not have built-in support for aspect-oriented programming, but it can be achieved using libraries or language extensions.

Paradigm can also be termed as a method to solve some problems or do some tasks. 
Paradigm is some strategy to solve that problem, it's the methodology/strategy.
'''


''' Object Oriented programming paradigms
In the object-oriented programming paradigm, objects are the key element of paradigms. 
but the major disadvantage of object-oriented programming paradigm is that if the code is not written properly then the program becomes a monster.


Advantages:
- Relation with Real world entities
- Code reusability
- Abstraction or data hiding

Disadvantages:
- Data protection
- Not suitable for all types of problems
- Slow Speed
'''
# class Emp has been defined here
class Emp:
    def __init__(self, name, age):
        self.name = name
        self.age = age
      
    def info(self):
        print("Hello, % s. You are % s old." % (self.name, self.age))
  
# Objects of class Emp has been 
# made here        
Emps = [Emp("John", 43),
    Emp("Hilbert", 16),
    Emp("Alice", 30)]
  
# Objects of class Emp has been
# used here
for emp in Emps:
    emp.info()
    
    

''' Procedural programming paradigms

In Procedure Oriented programming paradigms, series of computational steps are divided modules which means that the code is
grouped in functions and the code is serially executed step by step so basically, it combines the serial code to instruct a 
computer with each step to perform a certain task. 
modularization is usually done by the functional implementation.

Advantages
- General-purpose programming
- Code reusability
- Portable source code

Disadvantages
- Data protection
- Not suitable for real-world objects
- Harder to write

'''
# Procedural way of finding sum
# of a list

mylist = [10, 20, 30, 40]

# modularization is done by
# functional approach
def sum_the_list_ppp(mylist):
	res = 0
	for val in mylist:
		res += val
	return res

print(sum_the_list_ppp(mylist))



'''Functional programming paradigms

Functional programming paradigms is a paradigm in which everything is bind in pure mathematical functions style.
It is known as declarative paradigms because it uses declarations overstatements.
The paradigms mainly focus on “what to solve” rather than “how to solve”.
The ability to treat functions as values and pass them as an argument make the code more readable and understandable.


Advantages
- Simple to understand
- Making debugging and testing easier
- Enhances the comprehension and readability of the code

Disadvantages
- Low performance
- Writing programs is a daunting task
- Low readability of the code
'''
# Functional way of finding sum of a list
import functools


mylist = [11, 22, 33, 44]

# Recursive Functional approach
def sum_the_list(mylist):
	
	if len(mylist) == 1:
		return mylist[0]
	else:
		return mylist[0] + sum_the_list(mylist[1:])

# lambda function is used
print(functools.reduce(lambda x, y: x + y, mylist))
