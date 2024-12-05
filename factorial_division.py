# finds n! / d!
# note that n > d

def factorial_division(n, d):
    pro = 1
    
    for i in range(d+1, n+1):
        pro *= i
        
    return pro
