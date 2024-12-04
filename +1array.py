# adds 1 to the array
# [0,2,3]   >   [0,2,4]

def up_array(arr):
    b = 0
    if not arr:
        return None
    for i in arr:
        if i  > 9 or i < 0:
            return None
    for i in range(len(arr)):
        b += arr[i] * 10**(len(arr)-1-i)
    
    b = b + 1
    q = []
    for i in str(b):
        q.append(int(i))
    
    if arr[0] == 0 and len(arr) !=len(q):
        q.insert(0,0)
    return q
