# Read and Write to files.

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
f = open('test.txt', 'r+')
f.seek(0,2) # Go to byte 0 from the EOF. f.seek(offset, from_what)
f.write('\nSummer sun\n')
f.close()

# Write multiple lines to a file.
# w+ opens for read and write, but truncates any existing file first.
f = open('colors.txt', 'w+')
f.writelines([
    'red\n'
    'green\n'
    'blue\n'
])
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
