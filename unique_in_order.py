# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

def unique_in_order(sequence):
    q = []
    if not sequence:  # check if it is empty
        return []
    
    if len(sequence) == 1: # if length = 1 returns itself
        return [sequence[0]]
    
    for i in range(len(sequence)):
        if i+1 >=len(sequence): # do not be index out of range
            break
            
        if sequence[i] != sequence[i+1]:
                q.append(sequence[i])
                print(sequence[i])
                
    q.append(sequence[-1])
    
    return q
    
