# Printing output in color
class color:
   red = '\033[91m'
   green = '\033[92m'
   yellow = '\033[93m'
   end = '\033[0m'

print '%sThis is color%s' % (color.green, color.end)



# Shallow & deep equality
# http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap12.html

class Point:
   pass

p1 = Point()
p1.x = 3.0
p1.y = 5.0
p2 = Point()
p2.x = 3.0
p2.y = 5.0

# p1 and p2 contain the same coordinates, but are not the same object.
print p1 is p2 # False

# Shallow equality only compares references, not contents of objects.
# p1 and p2 are now aliases of the same object.
p1 = p2
print p1 is p2 # True
id(p1) # 40543152
id(p2) # 40543152

# Deep equality is two different objects that contain the same data.

def samePoint(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

p1 = Point()
p1.x = 3
p1.y = 4
p2 = Point()
p2.x = 3
p2.y = 4
print samePoint(p1, p2) # True

# Of course, if the two variables refer to the same object, they have both shallow and deep equality.



# Classes
# http://en.wikibooks.org/wiki/Python_Programming/Classes

# The first argument (methods must always take at least one argument) is always
# the instance of the class on which the function is invoked.

class Foo:
    def setx(self, x):
        self.x = x
    def bar(self):
        print self.x

# This constructs an instance of class Foo and creates a reference to it in f:
f = Foo()

# This invokes (calls) the methods in Foo:
f.setx(5)
f.bar() # 5

# Calling the methods on the object f:
Foo.setx(f,7)
Foo.bar(f) # 7

# Add a new member (y) to the Foo class.
Foo.y = 10
g = Foo()
print g.y # 10

# Class dictionaries:
vars(g) # {}
vars(f) # {'x': 7}

g.setx(5)
g.y = 9
print g.__dict__ # {'x': 5, 'y': 9}
g.__dict__['z'] = -4
print g.__dict__['z'] # -4

# Properties are attributes with getter and setter methods.
class SpamWithProperties(object):
    def __init__(self):
        self.__egg = "MyEgg"
    def get_egg(self):
        return self.__egg
    def set_egg(self, egg):
        self.__egg = egg
    egg = property(get_egg, set_egg)

sp = SpamWithProperties()
print sp.egg # 'MyEgg'
sp.egg = "Eggs With Spam"  # This sets the egg property
print sp.egg # 'Eggs With Spam'

# Class with @property decorator
class SpamWithProperties(object):
    def __init__(self):
        self.__egg = "MyEgg"
    @property
    def egg(self):
        return self.__egg
    @egg.setter
    def egg(self, egg):
        self.__egg = egg

print sp.egg # 'MyEgg'
sp.egg = "Eggs With Ham"
print sp.egg # 'Eggs With Ham'

# Static methods have no "self" argument and don't require you to instantiate the class before use.
class StaticSpam(object):
    def StaticNoSpam():
        print "You can't have have the spam, spam, eggs and spam without any spam... that's disgusting"
    NoSpam = staticmethod(StaticNoSpam)

StaticSpam.NoSpam()
# You can't have have the spam, spam, eggs and spam without any spam... that's disgusting

# Defined using the function decorator @staticmethod
class StaticSpam(object):
    @staticmethod
    def StaticNoSpam():
        print "You can't have have the spam, spam, eggs and spam without any spam... that's disgusting"

# Inheritance
class Foo:
    def bar(self):
        print "I'm doing Foo.bar()"
    x = 10

class Bar(Foo):
    def bar(self):
        print "I'm doing Bar.bar()"
        Foo.bar(self)
    y = 9

g = Bar()
Bar.bar(g)
# I'm doing Bar.bar()
# I'm doing Foo.bar()
print g.y # 9
print g.x # 10



# Classmethod and Staticmethod:
# https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner

# Both are ways of calling a method without instantiating the class.
# The classmethod's definition follows Sub class, not Parent class.
# It's first argument is cls.

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


date1 = Date.from_string('28-02-2019')
print date1.day # 28
Date.is_date_valid('28-02-2019') # True
