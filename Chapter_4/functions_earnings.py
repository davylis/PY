def compute_earnings(wage, hours):
    if hours<=40:
        pay=wage*hours
    elif hours>40:
        overtime=(hours-40)+(hours-40)/2
        pay=wage*40+overtime*wage
    return pay

def main():
    wage=float(input("Enter wage: "))
    hours=int(input("Enter hours: "))
    earnings=compute_earnings(wage, hours)
    print(f"The earnings are {earnings:.2f}")

if __name__ == "__main__":
    main()