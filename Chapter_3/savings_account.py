def savings():
    interest_rate=float(input("Enter interest rate: "))
    capital_income=float(input("Enter capital income tax rate: "))
    initial_deposit=float(input("Enter initial deposit: "))
    num_of_years=int(input("Enter number of years: "))
    print("")

    interest_rate*=0.01
    capital_income*=0.01

    for i in range(num_of_years):
     interest_of_the_year=initial_deposit*interest_rate
     tax_on_interest=interest_of_the_year*capital_income
     net_interest=interest_of_the_year-tax_on_interest

     initial_deposit+=net_interest

     year=i+1

     print(f"Year {year}: {initial_deposit:.2f}")

savings()