# Given an array of integers, find the one that appears an odd number of times.
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).

def find_it(seq):
    
    if len(seq) == 1:
        return seq[0]
    
    for i in seq:
        count = 0
        for j in seq:
            if j == i:
                count += 1
        if count % 2 != 0:
            return i
