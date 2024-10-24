def print_descending():
    try:
        num = int(input("Enter an integer: "))

        if num < 1:
            print("Nothing to be printed")
        else:
            total_sum=0
            for i in range(num, 0, -1):
                print(i, end=' ')
                total_sum+=i
            print()

            print("Sum: "+str(total_sum))
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print_descending()