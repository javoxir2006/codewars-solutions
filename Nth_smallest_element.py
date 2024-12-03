# arr = [4,3,6,0,1,5]  pos = 2
# arr = [0,1,3,4,5,6]
# returns arr[pos-1] = 1

def nth_smallest(arr, pos):
    for i in range(len(arr)):
        min_i = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        (arr[i], arr[min_i]) = (arr[min_i], arr[i])
    
    return arr[pos-1]
