def adjacent_element_product(array):
    high = array[0] * array[1] #making the first high
    
    for i in range(len(array)):
        if i+1 >= len(array):
            break  #breaking the loop when it exceeds the index
        if high < array[i]*array[i+1]:
            high = array[i]*array[i+1] #changing the high
        
    return high
