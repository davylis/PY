def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_circular_prime(n):
    num_str = str(n)
    num_len = len(num_str)

    for i in range(num_len):
        rotated_num = int(num_str[i:] + num_str[:i])
        if not is_prime(rotated_num):
            return False
    return True

def main():
    num = int(input("Enter a positive integer: "))

    if is_circular_prime(num):
        print(f"{num} is a circular prime")
    else:
        print(f"{num} is not a circular prime")

main()