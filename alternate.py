# 5, true, false     -->  [true, false, true, false, true]

def alternate(n, first_value, second_value):
    q = []
    for i in range(n):
        if i % 2 == 0:
            q.append(first_value)
        else:
            q.append(second_value)
            
    return q
