def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for c in r:
            print("{:d}".format(c), end=" " if column != r[-1] else "")
        print()
