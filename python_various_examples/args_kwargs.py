# args and kwargs
# Both allow you to pass a variable number of arguments to a function.
# **kwargs allows you to pass keyworded variable length of arguments to a function.

def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')
# ('first normal arg:', 'yasoob')
# ('another arg through *argv:', 'python')
# ('another arg through *argv:', 'eggs')
# ('another arg through *argv:', 'test')

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name="yasoob")
# name = yasoob
