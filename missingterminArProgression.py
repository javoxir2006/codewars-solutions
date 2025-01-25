# arithmetic progression
# find_missing([1, 3, 5, 9, 11]) == 7

def find_missing(sequence):
    
    full_sum = (sequence[-1] + sequence[0]) * (len(sequence) + 1) / 2 
    part_sum = sum(sequence)
    
    return full_sum - part_sum
