# Create a program called sharing_apples that first inputs
# the number of apples and the number of children. Then,
# the program should compute how many apples there are per
# child and how many leftover apples there will be. That is,
# each child should get the same number of apples.

apples = int(input("How many apples? "))
childrens = int(input("How many children? "))
          
leftover = apples % childrens
output = apples // childrens

print(f"Each child will get {output} apples.")
print(f"There will be {leftover} leftover apples.")