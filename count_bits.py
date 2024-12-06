# integer is converted to binary, and 1s is counted and returned
# The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def count_bits(n):
    bin = ""
    count = 0
    r = -1
    
    if n == 1:
        return 1
    
    while n >= 1:
        r = n % 2
        n -=r
        n/=2
        bin = bin + str(int(r))
    
    for i in bin:
        if i == "1":
            count += 1
            
    return count
        
