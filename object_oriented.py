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
# p1 and p2 have deep but not shallow equality.
print p1 is p2 # False
print id(p1) # 4585836984
print id(p2) # 4585837128

# Shallow equality only compares references, not contents of objects.
# p1 and p2 here become aliases of the same object.
# p1 and p2 have both deep and shallow equality.
p1 = p2
print p1 is p2 # True
print id(p1) # 4585837128
print id(p2) # 4585837128

p1.x = 64
print p2.x # 64
print p1 is p2 # True
print id(p1) # 4585837128
print id(p2) # 4585837128

# Deep equality is two different objects that contain the same data.
# Of course, if the two variables refer to the same object (have shallow equality),
# they have both shallow and deep equality.

def samePoint(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

p1 = Point()
p1.x = 7
p1.y = 15
p2 = Point()
p2.x = 7
p2.y = 15

# p1 and p2 have deep but not shallow equality.
print p1 is p2 # False
print samePoint(p1, p2) # True
