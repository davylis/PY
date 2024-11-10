def unique_int_list():
    integers=[]

    for element in range(5):
        integer=int(input("Enter an integer: "))
        integers.append(integer)

    distinct_sorted=sorted(set(integers))

    sorted_array=sorted(integers)

    print(", ".join(map(str, distinct_sorted)))

    print(", ".join(map(str, sorted_array)))

unique_int_list()