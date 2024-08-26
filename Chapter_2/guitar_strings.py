# Create a program called guitar_strings that calculates the
# total cost of guitar strings a guitarist will use on a set 
# of gigs.

#The program first inputs the total number of gigs the guitarist
# will do (integer), the number of gigs the guitarist plays 
# with the same set of strings, and the price of set of guitar 
# strings (float). Then, the program should compute and print 
# how many sets of guitar strings the guitarist will need and 
# the total cost of guitar strings with two decimal places.

#This time, we suppose that the guitarist must buy new guitar 
# strings if he is going to do any gigs.


numOfGigs = int(input("Number of gigs: "))
gigsToBePlayed = int(input("Gigs to be played with the same set of strings: "))
priceOfSet = float(input("Price of a set of guitar strings: "))

# int(-(-x // 1)) rounds up int because of negative num, even
# though float-point rounds int down
sets = int(-(-numOfGigs // gigsToBePlayed))
totalCost = priceOfSet * sets

print(f"\nThe guitarist needs {sets} new sets of guitar strings")
print(f"The total cost is {totalCost:.2f} euros")