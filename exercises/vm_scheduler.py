#!/usr/bin/env python
"""
VM scheduler
Determine the number of VMs needed based on the schedule.
"""

SCHEDULE1 = [(2,5),(3,6),(5,7)]
SCHEDULE2 = [(2,5),(3,6),(5,7),(5,8)]
SCHEDULE3 = [(2,5),(3,5),(5,7)]
SCHEDULE4 = []

def vm_schedule_count(vm_schedule):
    """
    The schedules contains reservations with start and end times.
    This function uses the sliding window technique.
    """
    trailing_res,leading_res = 0,0
    start,end = 0,1

    for reservation in vm_schedule:
        for previous_res in vm_schedule[trailing_res:leading_res]:
            if previous_res[end] <= reservation[start]:
                trailing_res += 1
                break
        leading_res += 1

    return len(schedule[trailing_res:leading_res])


schedules = [SCHEDULE1, SCHEDULE2, SCHEDULE3, SCHEDULE4]
for schedule in schedules:
    vm_count = vm_schedule_count(schedule)
    print(schedule, str(vm_count), "VMs")

# [(2, 5), (3, 6), (5, 7)] 2 VMs
# [(2, 5), (3, 6), (5, 7), (5, 8)] 3 VMs
# [(2, 5), (3, 5), (5, 7)] 2 VMs
# [] 0 VMs
