# returns true or false based on the fact that whether num is prime or not

def is_prime(num):
    if num < 2 :
        return False
    
    flag = 0
    i = 2
    
    while(i <= num/2):
        if(num % i == 0):
            flag = 1
            break
        i = i + 1
        
    if flag == 0:
        return True
    else:
        return False
  
