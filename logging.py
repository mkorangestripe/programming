import time
import timeit
import logging
import os
from os.path import expanduser
import sys

log_path = expanduser('~') + '/logs/'
timelog = log_path + 'timelog.log'

if os.path.isdir(log_path) == False:
  print log_path + " does not exist"
  sys.exit(1)

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(filename=timelog, level=logging.INFO, format=FORMAT)

def nothing():
  logging.info("starting first sleep")
  start_time = timeit.default_timer()
  time.sleep(5)
  elapsed = timeit.default_timer() - start_time
  logging.info("finished, elapsed time " + str(round(elapsed, 2)) + " seconds")

nothing()
