# [1,1,1,1,2,3,4,4]
# [1,4]
# returns [2,3]

def remove_(, integer_list, values_list):
        free = []
        for i in integer_list:
            if i not in values_list:
                free.append(i)
        return free
