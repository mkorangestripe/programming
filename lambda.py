# Lambda function/expressions:

# Combine first and last name into a single "Full Name":
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print full_name("  leonhard", "EULER")
# Leonhard Euler

# Sort list by last name:
scifi_authors = ["Isaac Asimov", "Ray Bradbury", "H. G. Wells"]

# Help on built-in function sort:
help(scifi_authors.sort)
# sort(...) method of builtins.list instance
#     L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*

scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print scifi_authors
# ['Isaac Asimov', 'Ray Bradbury', 'H. G. Wells']

# Quadratic function:
def build_quadric_function(a, b, c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

f = build_quadric_function(2, 3, -5)
print f(2)
# 9

print build_quadric_function(3, 0, 1)(2)  # 3x^2+1 evaluated for x=2
# 13
