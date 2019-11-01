# Simple threading example from Python for Unix and Linux System Administration, page 302
from threading import Thread
from time import sleep

count = 1

class KissThread(Thread):
    def run(self):
        global count
        print "Thread # %s:  Pretending to do stuff" % count
        count += 1
        sleep(2)
        print "done with stuff"

for t in range(5):
    KissThread().start()



# Threading example with loop outside function.
from threading import Thread
from time import sleep

def myfunc(i):
    print "sleeping 5 sec from thread %d" % i
    sleep(5)
    print "finished sleeping from thread %d" % i

for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()
t.join()
print "threads finished...exiting"



# Threading example with loop inside function.
from threading import Thread
from time import sleep

def threaded_function(arg):
    print arg
    for i in range(arg):
        print "running thread %s" % i
        sleep(1)

threads = Thread(target = threaded_function, args = (10,))
threads.start()
threads.join()
print "threads finished...exiting"
