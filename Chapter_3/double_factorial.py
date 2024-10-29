def double_factorial():
    try:
        n=int(input("Enter a non-negative integer: "))

        if n<0:
            print("Please enter a non-negative integer")
            return
        
        result=1

        for i in range(n, 0, -2):
            result*=i

        print(f"{n}!! = {result}")

    except:
        print("Please enter a valid integer")

double_factorial()