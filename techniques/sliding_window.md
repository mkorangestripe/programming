```python
SCHEDULE1 = [(2,5),(3,6),(5,7)]
SCHEDULE2 = [(2,5),(3,6),(5,7),(5,8)]
SCHEDULE3 = [(2,5),(3,5),(5,7)]
SCHEDULE4 = []
```

#### Basic structure

```python
vm_schedule = SCHEDULE2

trailing_res_i, leading_res_i = 0,0

for reservation in vm_schedule:
    print(f"Reservation: {reservation}")
    for prev_res in vm_schedule[trailing_res_i:leading_res_i]:
        print(prev_res)
    print()
    leading_res_i +=1
```

```
Reservation: (2, 5)

Reservation: (3, 6)
(2, 5)

Reservation: (5, 7)
(2, 5)
(3, 6)

Reservation: (5, 8)
(2, 5)
(3, 6)
(5, 7)
```

#### Actual sliding window technique

```python
vm_schedule = SCHEDULE2

trailing_res_i, leading_res_i = 0,0
start,end = 0,1

for reservation in vm_schedule:
    print(f"Reservation: {reservation}")
    for prev_res in vm_schedule[trailing_res_i:leading_res_i]:
        # print(f"Previous res: {prev_res}")
        if prev_res[end] <= reservation[start]:
            trailing_res_i += 1
            break
    print(f"Previous active res: {vm_schedule[trailing_res_i:leading_res_i]}")
    print()
    leading_res_i +=1

print(f"Number of VMs needed: {len(vm_schedule[trailing_res_i:leading_res_i])}")
```

```
Reservation: (2, 5)
Previous active res: []

Reservation: (3, 6)
Previous active res: [(2, 5)]

Reservation: (5, 7)
Previous active res: [(3, 6)]

Reservation: (5, 8)
Previous active res: [(3, 6), (5, 7)]

Number of VMs needed: 3
```
