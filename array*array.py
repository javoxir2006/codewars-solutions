# if (x) == ['a', 3] you should return [['a', 3], ['a', 3], ['a', 3]].

def explode(arr):  
    n = -1
    result = -1
    nums = [1,2,3,4,5,6,7,8,9,0]
    for i in range(2):
        if arr[0] in nums and arr[1] in nums:
            n = arr[0] + arr[1]
            result = [arr] * n
            break
        else:
            result = "Void!"
        if arr[0] in nums:
            n = arr[0]
            result = [arr] * n
            break
        if arr[1] in nums:
            n = arr[1]
            result = [arr] * n
            break
    return result
