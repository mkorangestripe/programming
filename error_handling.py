# try except statements
while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print "Not a valid number.  Try again..."


# try except statements with else and finally.
import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print 'cannot open', arg
    else:
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()
    finally:
        print "executing finally clause"


# Raise a runtime error:
raise RuntimeError('test for validate_request_parameters debug log')
