def strings_same_characters():
    str_one=input("Enter first string: ").replace(" ", "")
    str_two=input("Enter second string: ").replace(" ", "")

    if sorted(str_one) == sorted(str_two):
        print("Same characters")
    else:
        print("Different characters")

strings_same_characters()