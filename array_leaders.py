# An element is leader if it is greater than The Sum all the elements to its right side.
# arrayLeaders ({16, 17, 4, 3, 5, 2}) ==> return {17, 5, 2}

def array_leaders(numbers):
    arr = []
    
    for i in range(len(numbers)):
        sum = 0
        for j in range(i+1, len(numbers)):
            sum += numbers[j]
        if numbers[i] > sum:
            arr.append(numbers[i])
    return arr
