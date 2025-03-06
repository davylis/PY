def new_doubled_matrix(matrix):
    doubled_matrix=[]
    for row in matrix:
        new_row=[]
        for i in row:
            new_row.append(i*2)
        doubled_matrix.append(new_row)
    return doubled_matrix

def main():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = new_doubled_matrix(m1)
    print(m1)
    print(m2)
main()