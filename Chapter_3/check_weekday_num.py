def check_weekday():
    try:
        weekday=int(input("Enter a weekday number: "))
        if 1<= weekday <=7:
            print("OK")
        else:
             print("Please enter an integer between 1 and 7")
    except ValueError:
        print("Please enter an integer between 1 and 7")

check_weekday()
