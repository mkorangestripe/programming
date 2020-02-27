# Various examples

def vm_schedule_count(schedule):
    """Determine the number of VMs needed based on the schedule"""
    i,j = 0,0
    for times in schedule:
        start = times[0]
        for prev_times in schedule[i:j]:
            prev_end = prev_times[1]
            if prev_end <= start:
                i += 1
                break
        j += 1
    return len(schedule[i:j])


schedule1 = [(2,5),(3,6),(5,7)]
schedule2 = [(2,5),(3,6),(5,7),(5,8)]
schedule3 = [(2,5),(3,5),(5,7)]
schedule4 = []

vm_schedule_count(schedule1) # 2
vm_schedule_count(schedule2) # 3
vm_schedule_count(schedule3) # 2
vm_schedule_count(schedule4) # 0
