def multiply_by_two(array):
    for i in range(len(array)):
        array[i]*=2

def main():
    numbers = [1, 2, 3, 4, 5, 6]
    more_numbers = [10, 20, 30]
    print(numbers)
    multiply_by_two(numbers)
    print(numbers)
    print(more_numbers)
    multiply_by_two(more_numbers)
    print(more_numbers)
main()