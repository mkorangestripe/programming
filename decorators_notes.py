# Examples from linuxacademy.com using python 3

# Decorators...
# provide a simple syntax for calling higher-order functions.
# By definition, a decorator is a function that takes another function and...
# extends the behavior of the latter function without explicitly modifying it.

def inspect(func):
    def wrapped_func(*args, **kwargs):
        print(f"Running {func.__name__}")
        val = func(*args, **kwargs)
        print(f"Result: {val}")
        return val
    return wrapped_func

@inspect
def combine(a, b):
    return a + b

# When combine is called, inspect is called with combine as an argument...
# similar to running inspect(combine, 1, 2).

combine(1, b=2)
# Running combine
# Result: 3
# 3


# Classmethod, Staticmethod, and Property Decorators.

    class User:
        base_url = 'https://example.com/api'

        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name

        @classmethod
        def query(cls, query_string):
            return cls.base_url + '?' + query_string

        @staticmethod
        def name():
            return "Mike McClimber"

        # Above staticmethod without the decorator.
        # def name():
        #     return "Mike McClimber"
        # sname = staticmethod(name)

        @property
        def full_name(self):
            return f
            "{self.first_name} {self.last_name}"


# Classmethod
# Calls a method without instantiating the class.
# First argument is 'cls' the class itself.
# Has access to class level variables like 'base_url' above.
User.query('name=test')
# 'https://example.com/api?name=test'

# Staticmethod
# Call a method without instantiating the class.
# No access to the objects's state.
User.name()
# 'Mike McClimber'

# Property
# Instantiates the class.
user = User('Keith', 'Thompson')
user.base_url
# 'https://example.com/api'
# This method is not called, it's just referenced like user.base_url.
# Not 'user.full_name()'
user.full_name
# 'Keith Thompson'


# Another example of Classmethod and Staticmethod from...
# https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner

class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


# Classmethod
# The definition follows subclass, not Parent class...
# and a class is returned.
date1 = Date.from_string('28-02-2019')
print(date1.day)
# 28

# Staticmethod
Date.is_date_valid('28-02-2019')
# True
