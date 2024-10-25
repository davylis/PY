def check_month():
    while True:
        try:
            usr_input=input("Enter a month number: ")

            month=int(usr_input)

            if 1<= month <=12:
                print("OK")
                break
            else:
                print(f"{month} is not a valid month number\n")

        except ValueError:
            print(f"'{usr_input}' is not a valid month number\n")

check_month()