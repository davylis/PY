#Create a program called format_decimals that first inputs 
# a decimal value from the user. Then the program should 
# print the inputted value twice as shown in the example 
# output.

decimalNum = float(input("Enter a decimal number: "))
print(f"{decimalNum:.2f}")
print(f"{decimalNum:.4f}")