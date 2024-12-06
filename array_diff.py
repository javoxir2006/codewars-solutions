# It should remove all values from list a, which are present in list b keeping their order.
# array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(a, b):
    if a == []:
        return []
    x = []
    for i in a:
        if i not in b:
            x.append(i)
    return x
