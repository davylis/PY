def double_factorial(n):
    if n <= 1:
        return 1
    result=1
    for i in range(n, 0, -2):
        result*=i
    return result

def main():
    for i in range(10):
        print(f"{i}!! = {double_factorial(i)}")

if __name__ == "__main__":
    main()

