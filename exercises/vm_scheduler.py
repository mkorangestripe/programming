#!/usr/bin/env python
"""
VM scheduler
Determine the number of VMs needed based on the schedule.
"""

schedule1 = [(2,5),(3,6),(5,7)]
schedule2 = [(2,5),(3,6),(5,7),(5,8)]
schedule3 = [(2,5),(3,5),(5,7)]
schedule4 = []

def vm_schedule_count(vm_schedule):
    """
    The schedules contains reservations with start and end times.
    This function uses the sliding window technique.
    """
    trailing_res,leading_res = 0,0
    start,end = 0,1

    for reservation in vm_schedule:
        for prev_reservation in vm_schedule[trailing_res:leading_res]:
            if prev_reservation[end] <= reservation[start]:
                trailing_res += 1
                break
        leading_res += 1

    return len(schedule[trailing_res:leading_res])


schedules = [schedule1, schedule2, schedule3, schedule4]
for schedule in schedules:
    vm_count = vm_schedule_count(schedule)
    print(schedule, str(vm_count), "VMs")

# schedule1: 2 VMs
# schedule2: 3 VMs
# schedule3: 2 VMs
# schedule4: 0 VMs
