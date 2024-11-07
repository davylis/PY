def info():
    integers=[]

    for i in range (5):
        integer=int(input("Enter an integer: "))
        integers.append(integer)

    print("count: " + str(len(integers)))
    print("min:  "+ str(min(integers)))
    print("max:  "+ str(max(integers)))
    print("sum:  "+str(sum(integers)))

info()