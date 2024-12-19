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
    trailing_res_i, leading_res_i = 0,0
    start,end = 0,1

    for reservation in vm_schedule:
        print(f"Reservation: {reservation}")
        for previous_res in vm_schedule[trailing_res_i:leading_res_i]:
            print(f"  Window: {vm_schedule[trailing_res_i:leading_res_i+1]}")
            if previous_res[end] <= reservation[start]:
                trailing_res_i += 1
                print(f"  Window: {vm_schedule[trailing_res_i:leading_res_i+1]}")
                break
        leading_res_i += 1

    return len(vm_schedule[trailing_res_i:leading_res_i])


schedules = [SCHEDULE1, SCHEDULE2, SCHEDULE3, SCHEDULE4]
for schedule in schedules:
    print(f"Schedule: {schedule}")
    vm_count = vm_schedule_count(schedule)
    print(str(vm_count), "VMs")
    print()

# [(2, 5), (3, 6), (5, 7)]          2 VMs
# [(2, 5), (3, 6), (5, 7), (5, 8)]  3 VMs
# [(2, 5), (3, 5), (5, 7)]          2 VMs
# []                                0 VMs
