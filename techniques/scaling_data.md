# Scaling Data

Scaling data to fit between 0 and 1

```
Tooth types: Incisor, Canine, Premolar, Molar

Human Dental Formula:

Quadrant: 2I, 1C, 2P, 3M

Upper: 2.1.2.3
       -------
Lower: 2.1.2.3

Combined upper and lower:
Human               22112233
Wolf                33114423
Brown Bat           23113333
Rat                 22000066
```

```python
# The max tooth type count of all included animals:
max_types = [3,3,1,1,4,4,6,6]

max_reciprocals = [1/num for num in max_types]
```

```python
wolf = [3, 3, 1, 1, 4, 4, 2, 3]

# Multiply each tooth type count by its max reciprocal:
for i,tooth_type_cnt in enumerate(wolf):
    print(tooth_type_cnt * max_reciprocals[i])
```

```
1.0
1.0
1.0
1.0
1.0
1.0
0.3333333333333333
0.5
```

```python
rat = [2, 2, 0, 0, 0, 0, 6, 6]

for i,tooth_type_cnt in enumerate(rat):
    print(tooth_type_cnt *  max_reciprocals[i])
```

```
0.6666666666666666
0.6666666666666666
0.0
0.0
0.0
0.0
1.0
1.0
```
