def strings_digit_sum():
    sum = 0
    user = input("Enter a string: ")

    for char in user:
        if char.isdigit():
            sum+=int(char)   

    print(f"The sum of digits is {sum}") 

strings_digit_sum()
