# returns the last digit of n1 to the power n2

def last_digit(n1, n2):
    if n1 == 0 or n2 == 0:
        return 1
    
    r = n1 % 10
    m = n2 % 4
    
    if r == 0:
        return 0
    if m == 0:
        return r**4 % 10
    
    return r ** m % 10
