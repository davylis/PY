def strings_surnames():
    num_surnames=int(input("How many surnames? "))

    surnames = set()

    for i in range(num_surnames):
        surname=input("Enter a surname: ").strip()
        surnames.add(surname.lower())

    sorted_surnames=sorted(surnames)

    print()
    print(" ".join([surname.capitalize() for surname in sorted_surnames]))

strings_surnames()