# "This Is A Test" ==> "TIAT"

def make_string(s):
    x = s.split(" ")
    q = []
    
    for i in x:
        q.append(i[0])
        
        
    return "".join(i for i in q)
