def compute_discount(price, discount_perc):
    discount_perc/=100
    return price * discount_perc
    

def main():
    price=float(input("Enter price: "))
    discount_perc=float(input("Enter discount percentage: "))
    discount=compute_discount(price, discount_perc)
    print(f"The discount is {discount:.2f} euros")


if __name__ == "__main__":
    main()
