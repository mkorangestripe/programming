# VM scheduler
# Determine the number of VMs needed based on the schedule.

schedule1 = [(2,5),(3,6),(5,7)]
schedule2 = [(2,5),(3,6),(5,7),(5,8)]
schedule3 = [(2,5),(3,5),(5,7)]
schedule4 = []

def vm_schedule_count(schedule):
    """The schedule contains reservations with start and end times."""
    trailing_res,leading_res = 0,0
    start,end = 0,1

    for reservation in schedule:
        for prev_reservation in schedule[trailing_res:leading_res]:
            if prev_reservation[end] <= reservation[start]:
                trailing_res += 1
                break
        leading_res += 1

    return len(schedule[trailing_res:leading_res])


schedules = [schedule1, schedule2, schedule3, schedule4]
for schedule in schedules:
    vm_count = vm_schedule_count(schedule)
    print(schedule, str(vm_count))

# schedule1  # 2
# schedule2  # 3
# schedule3  # 2
# schedule4  # 0
