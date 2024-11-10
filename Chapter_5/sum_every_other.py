def sum_every_other(list): 
    if not list:
        return None
    
    return sum(list[::2])