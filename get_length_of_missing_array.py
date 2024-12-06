# You have to write a method, that return the length of the missing array.
# [[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3

def get_length_of_missing_array(array_of_arrays):
    
    if not array_of_arrays or [] in array_of_arrays:
        return 0
    
    for arr in array_of_arrays:
        if not arr or arr == None:
            return 0
            
    a = [len(i) for i in array_of_arrays]
    
    if not a:
        return 0
    
    a.sort()
    
    for i in range(a[0], a[-1] + 1):
        if i not in a:
            return i
