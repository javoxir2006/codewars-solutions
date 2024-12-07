# "indivisibility" -> 1 # 'i' occurs six times
# "aA11" -> 2 # 'a' and '1'

def duplicate_count(text):
    x = text.lower() 

    m = [] # will contain elements once
    
    for i in x:
        if i not in m:
            m.append(i) 
    
    dubs_count = 0
    for j in m:
        count_el = 0
        
        for i in x:
            if j == i:
                count_el +=1 # counts number of elements
        
        if count_el > 1:
            dubs_count +=1
            
    return dubs_count
    
    
    
    
            
    

    
    
    
    
    

     
