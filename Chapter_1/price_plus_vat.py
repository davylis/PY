# Create a program called price_plus_vat that first
#  inputs the price from the user. Then the program 
# should print the price with Value Added Tax (VAT) 
# added with two decimal places as shown in the example 
# output. Suppose that VAT is always 24 %.
# You should use  exception handling in this exercise.

try: 
    price = float(input("Enter price: "))
    vatRate = 0.24
    totalPrice = (price*vatRate)+price
    print(f"The price with VAT is {totalPrice:.2f}")
except ValueError:
    print("Invalid input. Enter a numeric value!")