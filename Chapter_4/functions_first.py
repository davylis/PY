def print_powers():
    num=1
    for i in range (20):
        print(num, end=" ")
        num*=2

def main():
    print_powers()

#Ensures that main() is called only when the script is executed directly, not when imported as a module.
if __name__ == "__main__":
    main()
