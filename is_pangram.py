# 

def is_pangram(st):
    iss = True
    a = "abcdefghijklmnopqrstuvwxyz"
    q =""
    x = st.lower()
    
    for i in x:
        if i in a:
            q += i

    for i in a:
        if i not in q:
            iss = False
            break
            
    return iss
            
