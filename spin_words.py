# if a length of word >= 5: returns its reversed version
# "Hey fellow warriors"  --> "Hey wollef sroirraw" 

def spin_words(sentence):
    x = sentence.split()
    h = []
    for i in x:
        if len(i) >= 5:
            m = ""
            for j in range(len(i) - 1,-1,-1):
                m = m + i[j]
                
            h.append(m)
        else:
            h.append(i)
    
    return " ".join(i for i in h)
