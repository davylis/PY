# Create a program called accurate_arithmetic that first inputs 
# two decimal numbers from the user. Then, the program should 
# print the sum of the decimal numbers as shown in the example 
# output.

# You are not required to set the number of decimal places in 
# the output.
from decimal import Decimal

decimalOne = Decimal(input("Enter first number: "))
decimalTwo = Decimal(input("Enter second number: "))

print(decimalOne + decimalTwo)