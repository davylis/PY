def reverse_desc():
    integers=[]

    for i in range (5):
        integer=int(input("Enter an integer: "))
        integers.append(integer)

    integers.sort(reverse=True)

    print(" ".join(map(str, integers)))

reverse_desc()