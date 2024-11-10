def remove_successive_duplicates(list):
    if not list:
        return
    
    i=1

    while i < len(list):
        if list[i] == list[i-1]:
            list.pop(i)
        else:
            i+=1

    