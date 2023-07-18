# from: https://www.youtube.com/watch?v=Ej_02ICOIgs

import csv


class Item:
    
    # class attribute will share among all instances
    pay_rate = 0.8 # 20 percent discount 
    all_item = []
    
    def __init__(self, name:str, price:float, quantity=0) -> None: # double underscore are magic methods :D
        
        # catch the bug early - assertion is cool 
        assert price >= 0, f"assertion: '{price} >= 0'  has failed!"
        assert quantity >=0, f"assertion: '{quantity} >= 0' has failed!"
        
        # assign to self object
        # there are instance attribute
        # single underscore means it will allow to be property - allow to be initialized - private variable
        # double underscore means it will be private - encapsulation
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        # action to execute
        Item.all_item.append(self) # Pay attention to Item -> It's class level -> class attribute
        
    @property
    def price(self):
        return self.__price
        
    def apply_discount(self):
        return self.__price * self.pay_rate # apply discount to price
    
    def apply_increment(self, increment_val):
        self.__price += self.__price * increment_val
        
    @property # read-only attribute ( without setter )
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value:str):
        value_length = len(value)
        # assert value_length >= 15, f"assertion: '{value_length} >= 15' has failed!"
        if value_length >= 15:
            raise Exception('The name is too long. should be equal or less than 15 chars!')
        else:
            self.__name = value
    
    def calc_total_price(self):
        return self.__price * self.quantity
   
    # u can also use double underscore to make the method private 
    def __some_private_method(self):
        print("IT'S A PRIVATE METHOD.")
    
    @classmethod
    def make_from_csv(cls):
        '''
        Class methods should do something that has a relationship with the class,
        but usually, those are used to manipluate different strcutures of data to instantiate objects,
        like this
        '''
        with open('OnlineResources/item_data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
            for item in items:
                Item(
                    name=item.get('name'), # type: ignore
                    price=float(item.get('price')), # type: ignore
                    quantity=int(item.get('quantity')) # type: ignore
                )
    
    @staticmethod # not passing the object as argument
    def is_integer(number):
        '''
        Static methods should do something that has a relationship with the class,
        but not something that must be unique per instance.
        '''
        # will count out the floats that are zero points like 3.0
        if isinstance(number, float):
            # count out the the floats that are point zero?
            return number.is_integer() #? what?
        elif isinstance(number, int):
            return True
        else:
            return False
    
    # magic method to how to represent an object - #! it's Dunder: Double Under(underscore)
    def __repr__(self) -> str:
        # with this approach u can easily create instance from copying and pasting just the repr magic method ;D
        # self.__class__.__name__ is the generic name to accessing class name - should work good with child classes
        return f"{self.__class__.__name__}('{self.__name}', {self.__price}, {self.quantity})" 
    


#* shift + tab will go backwards :D

# classmethod and staticmethod should be called from class level rather than instance level
    
item1 = Item('Phone', 500, 2)

# __dict__ will bring all attribute
# print(Item.__dict__) # class level 
# print(item1.__dict__) # instance level


# item1 = Item('Phone', 100, 1)
# item2 = Item('Laptop', 1000, 3)
# item3 = Item('Cable', 10, 5)
# item4 = Item('Mouse', 50, 5)
# item5 = Item('Keyboard', 75, 5)


Item.make_from_csv()
print(Item.all_item)
print(Item.is_integer(2.0))


# child class
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0) -> None:
        # call super to access to all attribute / methods of parent class
        super().__init__(name, price, quantity) 
        
        # assertion
        assert broken_phones >= 0, f"assertion: '{broken_phones} >= 0' has failed!"
        
        # assignment
        self.broken_phones = broken_phones
        
phone1 = Phone('test', 20,3,1)
print(Item.all_item)


'''OOP Principles

- Encapsulation:
    Restricting direct access to some of attributes, may change attribute using methods.

- Abstraction:
    Abstract information.
    Shows necessary attributes and hides unnecessary information. hide unnecessary details from user.

- Inheritance:
    resuse code across our classes. each child class have the same parent class but unique features.
    u can still use the code in the parent class for child instance class :D
    
- Polymorphism: -> poly:many  morphism:forms -> many forms
    use single type entity to represent different types in different scenarios. In differenct scenarios calling the exact same entity
    -> Apply to Entire Project. i.e: len() nuiltin function -> know how to handle different type of arguments like str, list, dict...
    
    
'''

# Dunder use for operator overloading
# u can use dir() function to see the dunders and methods 
# also it can list all functions inside a module

class Employee:
  def __new__(cls): # _> called before init for instantiate a new object -> first argument is class!
    print ("__new__ magic method is called")
    inst = object.__new__(cls)
    return inst

  def __init__(self):
    print ("__init__ magic method is called")
    self.name='Sa'
    
# from: https://www.tutorialsteacher.com/python/magic-methods-in-python
#? and: https://rszalski.github.io/magicmethods/ -> cool

'''
__str__(self)
Defines behavior for when str() is called on an instance of your class.

__repr__(self)
Defines behavior for when repr() is called on an instance of your class. 
The major difference between str() and repr() is intended audience. repr() is intended to produce output that is mostly machine-readable 
(in many cases, it could be valid Python code even), whereas str() is intended to be human-readable.
'''

#? Note: The private variables don't actually exist in Python. There are simply norms to be followed. The language itself doesn't apply any restrictions.

#* property(fget=None, fset=None, fdel=None, doc=None) / getter(), setter(), deleter(), comment