def surnames_list():
    surnames=[]
    
    while True:
        surname=input("Enter a surname (ok ends): ")

        if (surname == "ok"):
            break

        surnames.append(surname)

        

    distinct=list(set(surnames))
    sorted_surnames= sorted(distinct)

    print()
    print(", ".join(str(s) for s in sorted_surnames))

surnames_list()