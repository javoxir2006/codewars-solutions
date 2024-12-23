# find([3, 9, 1, 11, 13, 5]) # => 7

def find(seq):
    
    sum1 = (max(seq) + min(seq))*(len(seq)+1) / 2
    
    x = sum(seq)
    
    return sum1 - x
    
