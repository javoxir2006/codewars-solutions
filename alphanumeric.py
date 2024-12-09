# In this example you have to validate if a user input string is alphanumeric
# "PassW0rd", True

def alphanumeric(password):
    if not password:
        return False
    p = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    for i in password:
        if i not in p:
            return False
            break
    return True
