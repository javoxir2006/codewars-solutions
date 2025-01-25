# [[2,5], [3,5], [6,2]] is the same as [[2,6], [5,3], [2,5]] or [[3,5], [6,2], [5,2]]
# [[2,5], [3,6]] is NOT the same as [[2,3], [5,6]]

def same(arr_a, arr_b):
    if not arr_a or not arr_b:
        return True
    
    if len(arr_a) != + len(arr_b):
        return False
    count = 0 # it takes first subarray and finds same one on the second array and count += 1
              # next iteration, same
    for i in arr_a:
        for j in arr_b:
            if sorted(i) == sorted(j):
                count += 1
            
    if count == len(arr_a): # if count has same value as arr length returns True
        return True
    else:
        return False
