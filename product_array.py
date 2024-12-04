# productArray ({12,20}) ==>  return {20,12}
# The first element in prod [] array 20 is the product of all array's elements except the first element
# The second element 12 is the product of all array's elements except the second element .

def product_array(numbers):
    arr = []
    p = 1
    for i in range(len(numbers)):
        for j in numbers:
            p *= j
        p /= numbers[i]
        arr.append(int(p))
        p = 1
    return arr
