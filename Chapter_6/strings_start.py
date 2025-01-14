def string_start():
    user_input=input("Enter a string: ")

    print("\n"+user_input.lower())

    print(user_input.upper())

    print(f"{len(user_input)} characters")

def main():
    string_start()

if __name__ == "__main__":
    main()