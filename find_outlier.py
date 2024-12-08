# [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)
# [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

def find_outlier(integers):
    even = []
    odd = []
    
    for i in integers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
            
    if len(even) == 1:
        return even[0]
    
    if len(odd) == 1:
        return odd[0]
