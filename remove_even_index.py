# this was the first 😊
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

def remove_every_other(my_list):
    return [my_list[i] for i in range(0, len(my_list), 2)]
