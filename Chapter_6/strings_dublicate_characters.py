def strings_dublicate_characters():
    usr_str=input("Enter a string: ").strip()

    if len(usr_str) == len(set(usr_str)):
        print("No dublicates")
    else:
        print("Contains duplicate(s)")

strings_dublicate_characters()