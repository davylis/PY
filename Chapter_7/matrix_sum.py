def print_matrix_sum(m1, m2):
    for i in range(len(m1)):
        row_sum=[]
        for j in range(len(m1[i])):
            row_sum.append(m1[i][j] + m2[i][j])
        print(row_sum)

def main():
    m1 = [[1, 2, 0], [2, 3, 4]]
    m2 = [[3, 2, 5], [6, 4, 3]]
    m3 = [[1, 1, 1, 1], [3, 3, 2, 1], [2, 2, 2, 2]]
    m4 = [[2, 2, 2, 3], [2, 3, 1, 0], [1, 2, 3, 4]]

    print_matrix_sum(m1, m2)
    print()
    print_matrix_sum(m3, m4)

main()