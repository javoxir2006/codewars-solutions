# Given an array/list of n integers , find maximum triplet sum in the array Without duplications .
# maxTriSum ({3,2,6,8,2,3}) ==> return (17)
# As the triplet that maximize the sum {6,8,3} in order , their sum is (17)

def max_tri_sum(numbers):
    arr = []
    sum = 0
    
    for i in numbers:
        if i not in arr:
            arr.append(i)
            
    arr.sort()
    
    for j in range(1, 4):
        sum += arr[-j]
    
    return sum
