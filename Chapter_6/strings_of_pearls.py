def strings_of_pearls():
    pearl_count = 0

    user_input=input("Enter first string: ").strip()

    if user_input.lower() == "quit":
        print("Bye!")
        return
    
    while user_input.lower() != "quit":
        if user_input.lower() == "pearl":
            pearl_count += 1

        user_input = input("Enter next string: ").strip()

    print(f"\n{pearl_count} pearls")
    print("Bye!")

def main():
    strings_of_pearls()

if __name__ == "__main__":
    main()