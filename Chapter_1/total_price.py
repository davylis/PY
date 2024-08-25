# Create a program called total_price that first inputs 
# the price of the product and the handling fee (as integers) 
# from the user. Then the program should print the total price 
# as shown in the example output.

price = int(input("Enter price: "))
handlingFee = int(input("Enter handling fee: "))
totalPrice = price + handlingFee

print(f"The total price is {totalPrice}")