# maxProduct ({4, 3, 5}, 2) ==>  return (20)

def max_product(lst, n_largest_elements):
    pro = 1
    lst.sort()
    lst.reverse()
    for i in range(n_largest_elements):
        pro *= lst[i]
    return pro
