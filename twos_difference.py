# [1, 2, 3, 4]  should return [(1, 3), (2, 4)]

def twos_difference(lst): 
    result = []
    for i in range(len(lst)):
        if i+1 >= len(lst):
            break
            
        for j in range(i+1, len(lst)):
            if lst[i] - lst[j] == -2:
                result.append((lst[i], lst[j]))
                
            if lst[i] - lst[j] == 2:
                result.append((lst[j], lst[i]))
    result.sort()     
    return result
                
