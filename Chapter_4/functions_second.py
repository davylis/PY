def print_rectangle(w, h):
    for i in range (h):
        print('*'*w)

def main():
    h=int(input("Enter height: "))
    w=int(input("Enter width: "))

    print_rectangle(w, h)
 

if __name__ == "__main__":
    main()
