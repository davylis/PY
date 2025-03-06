def new_doubled_list(array):
    doubled_list = []
    for i in array:
        doubled_list.append(i*2)
    return doubled_list

def main():
    first_list = [1, 2, 3, 4, 5, 6]
    second_list = new_doubled_list(first_list)
    print(first_list)
    print(second_list)
main()