# n = 10  > n**2 = 100
# returns not!! because last digits don't equal 10
# n = 25  > n**2 = 625
# returns automorphic beacuse 25 == 25

def automorphic(n):
    is_ = "Automorphic"
    
    temp = [int(i) for i in str(n)]  # turns it into array
    temp.reverse() # to get the last digits
    
    tempsqrt = [int(i) for i in str(n**2)]
    tempsqrt.reverse()
    
    for i in range(len(temp)):
        if temp[i] != tempsqrt[i]:
            is_ = "Not!!"
    return is_
