# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

def narcissistic( value ):
    sum = 0
    x = str(value)
    
    for i in x:
        sum += int(i)**len(x)
    
    if sum == value:
        return True
    else:
        return False
   
