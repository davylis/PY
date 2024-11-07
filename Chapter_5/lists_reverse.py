def reverse():
    integers=[]

    how_many=int(input("How many integers? "))

    for i in range (how_many):
        integers.append(int(input("Enter an integer: ")))
    #join adds space, map converts each number to a 
    print(" ".join(map(str, integers[::-1])))

reverse()
