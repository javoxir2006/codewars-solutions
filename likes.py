# ["Peter"]  -->  "Peter likes this"

def likes(names):
    
    if names == []:
        return "no one likes this"
    if len(names) == 1:
        return names[0] + " likes this"
    if len(names) == 2:
        return " and ".join(i for i in names) + " like this"
    if len(names) == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    if len(names) >= 4:
        return names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"
