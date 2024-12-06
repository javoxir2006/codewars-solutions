# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

def create_phone_number(n):
    
    parent = ""
    for i in range(3):
        parent = parent + str(n[i])
        
    three = ""
    for i in range(3, 6):
        three = three + str(n[i])
        
    four = ""
    for i in range(6, 10):
        four = four + str(n[i])
        
    a ="("
    b = ") "
    return a + parent + b + three + "-" + four
