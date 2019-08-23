# Time in seconds since the epoch
import time
time.time() # 1554133995.335201

# Date in YYYYMMDD format
import time
date = time.strftime('%Y%m%d')
print date
# similar to 20190516

import datetime
now = datetime.datetime.now()
now_plus_one_day = now + datetime.timedelta(days = 1)
date_plus_one_day = now_plus_one_day.strftime('%Y%m%d%H%M')
print date_plus_one_day
# similar to 201905171155
