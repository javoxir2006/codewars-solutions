# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6

def digital_root(n):
    sum = 0
    
    for i in str(n):
        sum += int(i)
    
    if sum> 9:
        return digital_root(sum)
    else:
        return sum
