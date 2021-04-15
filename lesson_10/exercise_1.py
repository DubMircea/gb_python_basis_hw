class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        res = ''
        for row in self.matrix:
            res += f'{" ".join(map(str, row))}\n'

        return res

    def __add__(self, other):
        tmp_matrix = []
        if len(self.matrix) != len(other.matrix):
            raise ValueError('can not add different size matrix')
        for row_m, row_o in zip(self.matrix, other.matrix):
            if len(row_m) != len(row_o):
                raise ValueError('can not add different size matrix')
            tmp_matrix.append([i + j for i, j in zip(row_m, row_o)])

        return Matrix(tmp_matrix)


matrix_1 = Matrix([[1, -2, 3],
                   [4, 5, 6]])
print(matrix_1)
matrix_2 = Matrix([[1, 1, 1],
                   [2, 2, 2]])
print(matrix_2)

matrix_3 = matrix_1 + matrix_2
print(matrix_3)
