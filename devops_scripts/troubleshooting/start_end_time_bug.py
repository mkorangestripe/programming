## PBPRB-2492
## MAPI doesn't recognize start and end times properly

## Run this file from:
## ~/src/objectstorage-metrics-api/objectstorage_metrics_api/common

'''This is likely related to the fact that it straddles 2 months.  Example error:

curl -X POST "https://[CREDENTIALS REMOVED]"@"cos-metrics-us-south.storage.service.softlayer.net/resourcemetrics?start=1532995200000&end=1533081600000&resource_type=account&resource_id=ea48c4a22b2d44269f70d1793ab4e0c0&storage_location=us-south&storage_class=standard&metrics=average_byte_hours"

{"start": "1532995200000", "errors": ["Error trying to get value for average_byte_hours metric using data source, <objectstorage_metrics_api.common.cassandra_multilookup_metric_data_source.CassandraMultilookupMetricDataSource object at 0x7f624faeb2d0>. Exception: Start time should be less than end time"], "end": "1533081600000", "resource_type": "account", "warnings": [], "resources": []}

The times given for start and end are 2018-07-31 00:00:00 and 2018-08-01 00:00:00.'''


import time
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


print
print 'start_period: ' + str(start_period), time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(start_period/1000))
print 'end_period:   ' + str(end_period), time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(end_period/1000))
print

start_time = start_period

print 'datetime_util.py:90'
end_of_month_timestamp = DatetimeUtil.get_end_of_month_timestamp(start_time)
print "end_of_month_timestamp: " + str(end_of_month_timestamp), time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(end_of_month_timestamp/1000))
print

print 'cassandra_multilookup_metric_data_source.py:90'
## Modified slightly.
end_time = min(end_of_month_timestamp, end_period)
print 'end_time = min(end_of_month_timestamp, end_period): ' + str(end_time), time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(end_time/1000))
print

print 'cassandra_multilookup_metric_data_source.py:89-92'
print 'new_report_parameters.start_period: ' + str(start_time), time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(start_time/1000))
print 'new_report_parameters.end_period:   ' + str(end_time), time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(end_time/1000))
print

print 'cassandra_multilookup_metric_data_source.py:94'
start_time = end_time + 1
print "start_time = end_time + 1: " + str(start_time), time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(start_time/1000))
print

print 'cassandra_multilookup_metric_data_source.py:96'
## Modified slightly.
print 'start_time: ' + str(start_time), time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(start_time/1000))
print 'end_period: ' + str(end_period), time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(end_period/1000))
print 'start_time > end_period'
print start_time > end_period
print

print 'Next Iteration of While loop in _get_split_report_parameters...'
print

print 'start_time: ' + str(start_time), time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(start_time/1000))
print 'end_time:   ' + str(end_time), time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(end_time/1000))
print

print 'datetime_util.py:90'
end_of_month_timestamp = DatetimeUtil.get_end_of_month_timestamp(start_time)
print "end_of_month_timestamp: " + str(end_of_month_timestamp), time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(end_of_month_timestamp/1000))
print

print 'cassandra_multilookup_metric_data_source.py:90'
## Modified slightly.
end_time = min(end_of_month_timestamp, end_period)
print 'end_time = min(end_of_month_timestamp, end_period): ' + str(end_time), time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(end_time/1000))
print

print 'cassandra_multilookup_metric_data_source.py:89-92'
print 'new_report_parameters.start_period: ' + str(start_time), time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(start_time/1000))
print 'new_report_parameters.end_period:   ' + str(end_time), time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(end_time/1000))
print

print 'cassandra_multilookup_metric_data_source.py:94'
start_time = end_time + 1
print "start_time = end_time + 1: " + str(start_time), time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(start_time/1000))
print

print 'cassandra_multilookup_metric_data_source.py:96'
## Modified slightly.
print 'start_time: ' + str(start_time), time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(end_time/1000))
print 'end_period: ' + str(end_period), time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(end_period/1000))
print 'start_time > end_period'
print start_time > end_period

## At some point one of the following methods must be called (probably hour_timestamps_from_to)...
## and probably called by something that uses the split_report_parameters list.
## Both methods have the message, 'Start time should be less than end time'.
## datetime_util.py:DatetimeUtil.hour_timestamps_from_to
## datetime_util.py:DatetimeUtil.hour_timestamps_after_to

## The proposed fix is to change the '>' to '>=' in lines with...
## 'start_time > reports_parameters.end_period' as shown below.
## This works depending on what's expected from start_time/end_time inclusion.

print
print

class reports_parameters_testing:
    ## Tuesday, July 31, 2018 12:00:00 AM GMT
    start_period = 1532995200000
    ## Wednesday, August 1, 2018 12:00:00 AM GMT
    end_period = 1533081600000
    ## Saturday, September 15, 2018 12:00:00 AM GMT
    #end_period = 1536969600000


def _get_split_report_parameters(reports_parameters):
    """Get list of ReportsParameters broken up by time period

    For each month in the time period established by the start and end
    periods provided by the ReportsParameters object, breaks the
    provided ReportsParameters object into smaller bits - one per month.
    Each object in the list of ReportsParameters is the same except for
    their time periods.

    :param reports_parameters: ReportsParameters - Contains data required
        to calculate the value of the metric such as start_period.
    :return: Array<ReportsParameters>

    """
    split_report_parameters = []

    start_time = reports_parameters.start_period
    while True:
        #new_report_parameters = reports_parameters.copy() ## commented out for testing PBPRB-2492
        class new_report_parameters: pass ## added for testing PBPRB-2492
        new_report_parameters.start_period = start_time
        end_time = min(DatetimeUtil.get_end_of_month_timestamp(start_time),
                       reports_parameters.end_period)
        new_report_parameters.end_period = end_time
        split_report_parameters.append(new_report_parameters)
        start_time = end_time + 1

        if start_time > reports_parameters.end_period:
            break

    log_line = {'timestamp': time.time(),
                'message': 'Finished splitting report parameters',
                'split_report_parameters': str(split_report_parameters)}
    #log_debug(log_line) ## commented out for testing PBPRB-2492

    return split_report_parameters


def _get_split_report_parameters_proposed(reports_parameters):
    """Get list of ReportsParameters broken up by time period

    For each month in the time period established by the start and end
    periods provided by the ReportsParameters object, breaks the
    provided ReportsParameters object into smaller bits - one per month.
    Each object in the list of ReportsParameters is the same except for
    their time periods.

    :param reports_parameters: ReportsParameters - Contains data required
        to calculate the value of the metric such as start_period.
    :return: Array<ReportsParameters>

    """
    split_report_parameters = []

    start_time = reports_parameters.start_period
    while True:
        #new_report_parameters = reports_parameters.copy() ## commented out for testing PBPRB-2492
        class new_report_parameters: pass ## added for testing PBPRB-2492
        new_report_parameters.start_period = start_time
        end_time = min(DatetimeUtil.get_end_of_month_timestamp(start_time),
                       reports_parameters.end_period)
        new_report_parameters.end_period = end_time
        split_report_parameters.append(new_report_parameters)
        start_time = end_time + 1

        if start_time >= reports_parameters.end_period: ## proposed change for PBPRB-2492
            break

    log_line = {'timestamp': time.time(),
                'message': 'Finished splitting report parameters',
                'split_report_parameters': str(split_report_parameters)}
    #log_debug(log_line) ## commented out for testing PBPRB-2492

    return split_report_parameters


split_report_parameters =  _get_split_report_parameters(reports_parameters_testing)

print 'Results from _get_split_report_parameters:'
for new_report_parameters in split_report_parameters:
    print 'new_report_parameters.start_period', new_report_parameters.start_period
    print 'new_report_parameters.end_period  ', new_report_parameters.end_period
print

split_report_parameters =  _get_split_report_parameters_proposed(reports_parameters_testing)

print 'Results form proposed change to _get_split_report_parameters:'
for new_report_parameters in split_report_parameters:
    print 'new_report_parameters.start_period', new_report_parameters.start_period
    print 'new_report_parameters.end_period  ', new_report_parameters.end_period
