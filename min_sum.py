# Given an array of integers , Find the minimum sum which is obtained from summing each Two integers product .
# minSum({5,4,2,3}) ==> return (22) 
# The minimum sum obtained from summing each two integers product ,  5*2 + 3*4 = 22

def min_sum(arr):
    min_sum = 0
    
    arr.sort()
    
    for i in range(int(len(arr)/2)):
        min_sum += arr[i] * arr[-i-1]

    return min_sum
