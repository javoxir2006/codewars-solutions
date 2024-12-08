# Input = "The sunset sets at twelve o' clock."
# Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

def alphabet_position(text):

    low = text.lower()
    al = "abcdefghijklmnopqrstuvwxyz"
    a = []
    
    for let in low:
        if let in al:
            a.append(let) 
    
    m = []        
    
    for i in a:
        b = al.index(i)
        m.append(str(b+1))
        
    return " ".join(i for i in m)
