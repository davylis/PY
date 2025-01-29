def strings_slicing_5():
    usr_str=input("Enter a string: ")
    usr_char=input("Enter a character: ")

    #preventing out-of-bounds slicing
    for i in range(len(usr_str)-3):
        if usr_str[i]==usr_char:
            print(usr_str[i:i+4])

strings_slicing_5()