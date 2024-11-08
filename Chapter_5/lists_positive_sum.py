def positive_sum(integers):
    if sum(integers) == 0:
        print()
        print("0")
    else:
        print()
        print(sum(integers))

def main():
    integers=[]

    for i in range(5):
        integer=int(input("Enter an integer: "))

        if integer>0:
            integers.append(integer)

    positive_sum(integers)

if __name__ == "__main__":
    main()