## platform
## Access to underlying platform's identifying data.
import platform
platform.node() # network name, also socket.gethostname()
platform.system() # operating system
platform.dist() # distro
platform.uname() # like uname -a

## os
## Operating System dependent functionality.
import os

## mkdir /tmp/dirA
## touch /tmp/dirA/file1.txt /tmp/dirA/file00.txt /tmp/dirA/file0.txt
## mkdir /tmp/dirB
## touch /tmp/dirB/file1.txt /tmp/dirB/file00.txt /tmp/dirB/file11.txt /tmp/dirB/file0.txt
dirA = set(os.listdir("/tmp/dirA"))
dirB = set(os.listdir("/tmp/dirB"))
## dirB is a superset of dirA.  dirA - dirB will return an empty result.
## this only accounts for filenames, not content
print dirA - dirB
print dirB - dirA

os.chdir("/tmp")
os.getcwd()
os.stat("/tmp")
os.makedirs("/tmp/os_mod_explore/test_dir1")
os.rename("/tmp/os_mod_explore/test_dir1", "/tmp/os_mod_explore/test_dir1_renamed")
os.makedirs("test/test_subdir1/test_subdir2")
os.listdir("/tmp")
os.listdir(os.getcwd())

import shutil
shutil.copytree("test", "test-copy")
shutil.move("test-copy", "test-copy-moved")
shutil.rmtree("test-copy-moved")
shutil.rmtree("test")
shutil.rmtree("/tmp/os_mod_explore")

## subprocess
## Spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
import subprocess

## Calling a system command.
subprocess.call(['df', '-h'])

## Calling a system command and a shell variable.
subprocess.call("df -h $HOME", shell=True)

## Just outputting the exit status (return code).
ret = subprocess.call("ping -c 1 127.0.0.1",
shell=True,
stdout=open('/dev/null', 'w'),
stderr=subprocess.STDOUT)

## Capturing Standard out.
p = subprocess.Popen("df -h", shell=True, stdout=subprocess.PIPE)
out = p.stdout.readlines()
for line in out:
    print line.strip()

## Subprocess piping factory.
def multi(*args):
    for cmd in args:
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        out = p.stdout.read()
        print out

multi("df -h", "ls -l /tmp", "dmesg | tail")

## System specific parameters and functions.
import sys
print sys.argv # all command line arguments.
print sys.argv[0] # the script itself.
print sys.argv[1] # first command line argument passed to the script.
sys.exit()


## Argument and options.
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int, choices=[0,1,2],
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2

if args.verbosity == 2:
    print "the square of {0} equals {1}".format(args.square, answer)
elif args.verbosity == 1:
    print "{0}^2 == {1}".format(args.square, answer)
else:
    print answer


## raw_input a string.
s = raw_input('Enter a number: ')
## raw_input an int.
n = int(raw_input('Enter a number: '))
type(s) # <type 'str'>
type(n) # <type 'int'>

## input() - python 2.x
## Equivalent to eval(raw_input(prompt))
## Consider using the raw_input() function for general input from users.

## input a string.
s = str(input('Enter a number: '))
## input an int.
n = input('Enter a number: ')
type(s) # <type 'str'>
type(n) # <type 'int'>

## input() evaluates the input.
c1 = 'sky blue'
c2 = 'brick red'
color = input('Enter a color: ')

## Read and Write to files.

## Print the file as one string.
f = open('test.txt')
f.readline() #print just one line.
f.read() #print all lines.
f.close()

## Position in file.
f = open('test.txt')
f.read(27) # Print the first 27 bytes.
f.tell() # Check the file object's current position in the file.
f.seek(0) # Set current position to byte 0 (beginning of file).
f.close()

## Print the file as a list.
f = open('test.txt')
f.readlines()
f.close()

## Print the lines individually.
f = open('test.txt')
for line in f:
    print line,
f.close()

## Using the 'with' ensures that the file is properly closed after its suite finishes.
with open('test.txt', 'r') as f:
    read_data = f.read()
print f.closed # True

## Appending to a file.  a+ opens for read and append.
## Note, tail -f test.txt # The file isn't updated until tell, seek, close, etc.
##
f = open('test.txt', 'a+')
f.write('\nWinter snow\n')
f.close()

## Append or write to a file at any byte. r+ opens for read and write.
## w+ opens for read and write, but truncates any existing file first.
f = open('test.txt', 'r+')
f.seek(0,2) # Go to byte 0 from the EOF. f.seek(offset, from_what)
f.write('\nSummer sun\n')
f.close()

## Simple serialization, saving data objects to disk.
## cPickle is an optimized version written in C, but does not support subclassing.
import pickle

## Write a dict to disk.
dict1 = {'a': 1, 'b': 2, 'c': 3}
pickle_file = open('dict1.pkl', 'w')
pickle.dump(dict1, pickle_file)
pickle_file.close()

## Read the dict from disk.
pickle_file = open('dict1.pkl', 'r')
dict2 = pickle.load(pickle_file)
