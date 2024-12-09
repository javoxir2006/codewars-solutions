def sum_strings(x, y):
    sum = 0
    print(y)
    
    if x == "" and y =="":
        return "0"
    if x == "" or y =="":
        return x+y
    else:
        return str(int(x) + int(y))
