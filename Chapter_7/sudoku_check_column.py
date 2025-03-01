def column_ok(sudoku, index):
    seen_numbers=set()

    for row in sudoku:
        num = row[index]
        if num in seen_numbers and num != 0:
            return False
        seen_numbers.add(num)

    return True

def main():
sudoku = [
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
print(column_ok(sudoku, column_index=0)) # False
print(column_ok(sudoku, column_index=1)) # True
print(column_ok(sudoku, column_index=8)) 