def row_ok(sudoku, index):
    row = sudoku[index]
    seen=set()

    for num in row:
        if num != 0:
            if num in seen:
                return False
            seen.add(num)
    return True

def column_ok(sudoku, index):
    seen_numbers=set()

    for row in sudoku:
        num = row[index]
        if num in seen_numbers and num != 0:
            return False
        seen_numbers.add(num)
    return True

def block_ok(sudoku, row_index, column_index):
    valid_grid = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

    if (row_index, column_index) not in valid_grid:
        return False
    
    seen_numbers=set()

    for i in range(row_index, row_index + 3):
        for j in range(column_index, column_index + 3):
            num = sudoku[i][j]
            if num !=0:
                if num in seen_numbers:
                    return False
                seen_numbers.add(num)
    return True


def grid_ok(sudoku):
    for i in range(9):
        if not row_ok(sudoku, i):
            return False
        
    for j in range(9):
        if not column_ok(sudoku, j):
            return False
        
    block_start_positions = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for (i, j) in block_start_positions:
        if not block_ok(sudoku, i, j):
            return False
    return True

def main():
    sudoku_1 = [
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    sudoku_2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(grid_ok(sudoku_1)) # False
    print(grid_ok(sudoku_2)) # True
if __name__ == "__main__":
    main()