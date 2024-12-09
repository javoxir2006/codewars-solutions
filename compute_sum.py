# N = 10
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46

def compute_sum(n):
    sum =0
    for i in range(1, n+1):
        if i < 10:
            sum+= i
        else:
            for j in str(i):
                sum+=int(j)
    return sum
