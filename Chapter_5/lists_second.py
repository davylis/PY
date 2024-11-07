def alphabetical_order():
    words=[]

    while True:
        word=input("Enter a word (quit ends): ")

        if word == "quit":
            break

        words.append(word)

    words.sort()

    for word in words:
        print(word)


alphabetical_order()