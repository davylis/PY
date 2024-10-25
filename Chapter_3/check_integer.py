def check_int():
    usr_input=input("Enter an integer: ")

    try:
        integer=int(usr_input)
        print("OK")
    except ValueError:
        print("'" + usr_input+ "'" + " is not an integer")

check_int()