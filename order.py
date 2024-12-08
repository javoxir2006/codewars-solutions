# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"

def order(sentence):
    if not sentence:
        return ""
    
    num = "123456789"
    index = -1
    x = sentence.split(" ")
    m = [None] * len(x)
    for i in x:
        for j in i:
            if j in num:
                index = int(j) - 1
                m[index] = i
    return " ".join(m)
    
  
