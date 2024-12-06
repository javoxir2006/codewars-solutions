# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2

def find_uniq(arr):
    
    arr.sort()
    
    if arr[0] != arr[1]:
        return arr[0]
    
    if arr[-1] != arr[-2]:
        return arr[-1]
