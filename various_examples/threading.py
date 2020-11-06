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



# Ping without using threading.
# Example from Python for Unix and Linux System Administration, page 302.
# This seems to run in only one process according to the following command.  Filename ping_no_thread.py
# while true; do ps -ef | grep ping_ | grep -v grep; sleep 1; done
import subprocess
import time

IP_LIST = [
'yahoo.com',
'yelp.com',
'amazon.com',
'freebase.com',
'clearink.com',
'ironport.com']

cmd_stub = 'ping -c 5 %s'

def do_ping(addr):
  print time.asctime(), "DOING PING FOR", addr
  cmd = cmd_stub % (addr,)
  return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

z = []
for ip in IP_LIST:
  p = do_ping(ip)
  z.append((p, ip))

for p, ip in z:
  print time.asctime(), "WAITING FOR", ip
  p.wait()
  print time.asctime(), ip, "RETURNED", p.returncode



# Ping using threading.
# Example from Python for Unix and Linux System Administration, page 303.
from threading import Thread
import subprocess
from Queue import Queue

num_threads = 3
queue = Queue()
ips = ["192.168.1.1", "192.168.1.110", "192.168.1.111", "192.168.1.112", "192.168.1.113"]

def pinger(i, q):
    """Pings subnet"""
    while True:
        ip = q.get()
        print "Thread %s: Pinging %s" % (i, ip)
        ret = subprocess.call("ping -c 4 %s" % ip,
                        shell=True,
                        stdout=open('/dev/null', 'w'),
                        stderr=subprocess.STDOUT)
        if ret == 0:
            print "%s: is alive" % ip
        else:
            print "%s: did not respond" % ip
        q.task_done()

for i in range(num_threads):
    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()

for ip in ips:
    queue.put(ip)

print "Main Thread Waiting"
queue.join()
print "Done"
