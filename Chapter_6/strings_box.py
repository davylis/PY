def strings_box():
    usr_str=input("Enter a string: ").strip()

    box_width=len(usr_str) + 4
    print('-'*box_width)
    print(f"| {usr_str} |")
    print('-'*box_width)

strings_box()
