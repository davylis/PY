# Create a program called gym_exercise that first inputs the 
# number of days when the user visits the local gym per year, 
# the yearly membership fee, and the price of the day pass. 
# Then, the program should determine which one is the cheaper 
# option (paying the yearly membership fee or buying separate 
# day passes) and how much cheaper it is.

# The program should display one of the following texts:
# -Buying day passes is 99.00 euros cheaper
# -Paying the yearly membership fee is 99.00 euros cheaper
# -There is no price difference

daysInGym = int(input("Enter the number of days of gym visits per year: "))
priceForADayPass = float(input("Enter price for a day pass: "))
yearlyMembership = float(input("Enter yearly membership fee: "))

dayPass = daysInGym * priceForADayPass

if dayPass > yearlyMembership:
    output = dayPass - yearlyMembership
    print(f"\nPaying the yearly membership fee is {output:.2f} euros cheaper")

elif yearlyMembership > dayPass:
    output = yearlyMembership - dayPass
    print(f"\nPaying the yearly membership fee is {output:.2f} euros cheaper")
else:
    print("\nThere is no price difference")