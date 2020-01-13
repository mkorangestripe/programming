## PBPRB-2532
## MAPI Datetime Conversion Adds an Hour

## The required modules datetime_util and util can be found:
##  ~/src/objectstorage-metrics-api/objectstorage_metrics_api/common

## The following three methods in datetime_util.py add an hour when converting the datetime format.
## DatetimeUtil.convert_from_timestamp
## DatetimeUtil.convert_from_timestamp_to_datetime
## DatetimeUtil.truncate_timestamp_to_month

## This conversion adds an hour to the timestamp during DST which could be a problem if the start_time were within the last hour of the month.
## datetime.datetime.fromtimestamp(int(time.mktime(time.gmtime(1531694299)))).strftime("%Y-%m-%d %H:%M:%S")
## '2018-07-15 23:38:19'
## This should be 22:38:19

## The time.gmtime function converts Epoch time correctly, but leaves Daylight Savings Time set to false.
## time.gmtime(1531694299)
## time.struct_time(tm_year=2018, tm_mon=7, tm_mday=15, tm_hour=22, tm_min=38, tm_sec=19, tm_wday=6, tm_yday=196, tm_isdst=0)
## When converting back to Epoch time, the time.mktime function add six hours.
## time.mktime(time.gmtime(1531694299))
## 1531715899.0 (This is July 16, 2018 4:38:19 AM GMT)
## The datetime.datetime.fromtimestamp function then subtracts 5 hours.
## datetime.datetime.fromtimestamp(int(time.mktime(time.gmtime(1531694299))))
## datetime.datetime(2018, 7, 15, 23, 38, 19)

## This converts corectly and outputs the same format:
## gmtime = time.gmtime(1531694299)
## datetime.datetime(gmtime.tm_year, gmtime.tm_mon, gmtime.tm_mday,gmtime.tm_hour, gmtime.tm_min, gmtime.tm_sec)
## datetime.datetime(2018, 7, 15, 22, 38, 19)


import time
import datetime
from datetime_util import DatetimeUtil

## Testing with start_time and end_time in different months...
## Tuesday, July 31, 2018 12:00:00 AM GMT
start_period = 1532995200000
## Wednesday, August 1, 2018 12:00:00 AM GMT
end_period = 1533081600000

## Testing with start_time and end_time in the same month...
## Sunday, July 15, 2018 10:38:19 PM GMT
#start_period = 1531694299000
## Monday, July 30, 2018 10:55:10 PM GMT
#end_period = 1532991310000



def truncate_timestamp_to_month(timestamp):
    """Convert timestamp to string.

    :param timestamp: int - UTC timestamp
    :return: string - String version of the UTC timestamp

    """
    if DatetimeUtil.PRECISION == 'millisecond':
        timestamp = timestamp / 1000
    return datetime.datetime.fromtimestamp(
        int(time.mktime(
            time.gmtime(timestamp)))).strftime("%Y-%m")



def convert_from_timestamp(timestamp):
    """Convert timestamp to string.

    :param timestamp: int - UTC timestamp
    :return: string - String version of the UTC timestamp

    """
    if DatetimeUtil.PRECISION == 'millisecond':
        timestamp = timestamp / 1000
    return datetime.datetime.fromtimestamp(
        int(time.mktime(
            time.gmtime(timestamp)))).strftime("%Y-%m-%d %H:%M:%S")



def convert_from_timestamp_to_datetime(timestamp):
    """Convert timestamp to datetime.

    :param timestamp: int - UTC timestamp
    :return: datetime - datetime version of the UTC timestamp

    """
    if DatetimeUtil.PRECISION == 'millisecond':
        timestamp = timestamp / 1000
    return datetime.datetime.fromtimestamp(
        int(time.mktime(
            time.gmtime(timestamp))))



timestamp = start_period

truncate_timestamp_to_month = truncate_timestamp_to_month(timestamp)
truncate_timestamp_to_month_new = DatetimeUtil.truncate_timestamp_to_month(timestamp)

convert_from_timestamp = convert_from_timestamp(timestamp)
convert_from_timestamp_new = DatetimeUtil.convert_from_timestamp(timestamp)

convert_from_timestamp_to_datetime = convert_from_timestamp_to_datetime(timestamp)
convert_from_timestamp_to_datetime_new = DatetimeUtil.convert_from_timestamp_to_datetime(timestamp)

print
print 'timestamp:', timestamp
print
print 'truncate_timestamp_to_month:    ', truncate_timestamp_to_month, type(truncate_timestamp_to_month)
print 'truncate_timestamp_to_month_new:', truncate_timestamp_to_month_new, type(truncate_timestamp_to_month_new)
print
print 'convert_from_timestamp:    ', convert_from_timestamp, type(convert_from_timestamp)
print 'convert_from_timestamp_new:', convert_from_timestamp_new, type(convert_from_timestamp_new)
print
print 'convert_from_timestamp_to_datetime:    ', convert_from_timestamp_to_datetime, type(convert_from_timestamp_to_datetime)
print 'convert_from_timestamp_to_datetime_new:', convert_from_timestamp_to_datetime_new, type(convert_from_timestamp_to_datetime_new)
