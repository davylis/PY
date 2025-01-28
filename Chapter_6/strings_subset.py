def strings_subset():
    first_str=input("Enter first string: ").lower()
    second_str=input("Enter second string: ").lower()

    if not second_str:
        print("Nothing to be checked")
        return
    
    is_subset=True

    for char in second_str:
        if char not in first_str:
            is_subset=False
            break

    if is_subset:
        print("Subset")
    else:
        print("Not subset")

strings_subset()