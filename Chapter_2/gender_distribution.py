# Create a program called gender_ distribution that first
#  inputs the number female students and the number of male
#  students from the user. Then, the program should calculate
#  the percentage of female students and the percentage of
#  male students. The program should show the percentages
#  with one decimal place.

females = int(input("Enter the number of female students: "))
males = int(input("Enter the number of male students: "))

if females + males == 0:
    totalMale = 0.0
    totalFemale = 0.0
else:
    totalFemale = females/(females+males)*100
    totalMale = males/(females+males)*100

print(f"Female: {totalFemale:.1f} %")
print(f"Male: {totalMale:.1f} %")


  