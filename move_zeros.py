# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    q = []
    n = []
    for i in lst:
        if i == 0:
            q.append(i)
        else:
            n.append(i)
    for i in q:
        n.append(i)
    return n
            
