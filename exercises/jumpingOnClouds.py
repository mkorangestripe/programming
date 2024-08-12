#!/usr/bin/env python
"""
Jumping On Clouds
Start with an array of clouds where cumulus are safe and thunderheads must be avoided.
cumulus = 0, thunderheads = 1
The first and last elements are 0 (cumulus).
Move from first to last but only by one or two clouds per jump.
"""

def jumpingOnClouds(c):
    def jumpingOnClouds_helper(c, i=0, jumps=1):
        if len(c[i:]) <= 3:
            return (c, i, jumps)
        if c[i+2] == 0:
            i+=2
        else:
            i+=1
        jumps += 1
        return jumpingOnClouds_helper(c,i,jumps)
    c,i,jumps = jumpingOnClouds_helper(c)
    return jumps

c = [0, 0, 1, 0, 0, 1, 0]
jumps = jumpingOnClouds(c)
print("Jumps:", jumps)