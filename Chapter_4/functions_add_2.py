def add(f_one, f_two):
    sum = f_one+f_two
    return int(sum+0.5)

def main():
    f_one=float(input("Enter a float: "))
    f_two=float(input("Enter a float: "))
    result=add(f_one, f_two)
    print(result)

if __name__ == "__main__":
    main()