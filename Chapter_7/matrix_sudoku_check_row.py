def row_ok(matrix, index):
    row = matrix[index]
    seen=set()

    for num in row:
        if num != 0:
            if num in seen:
                return False
            seen.add(num)


    return True

def main():
    matrix = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(row_ok(matrix, index=0)) # True
    print(row_ok(matrix, index=1)) # False
    print(row_ok(matrix, index=8)) # True


if __name__ == "__main__":
    main()