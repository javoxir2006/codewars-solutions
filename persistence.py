# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)

def persistence(n):
    
    c = 0
    
    while n > 9:
        r = 1
        
        for i in str(n):
            r *= int(i)
            
        c = c + 1
        n = r
         
    return c
