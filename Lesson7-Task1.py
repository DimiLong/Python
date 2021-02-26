class Matrix:
    def __init__(self, sourceData):
        self.__matrix = sourceData
    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.__matrix]))
    def __add__(self, matrix):
        ret = Matrix(self.__matrix)
        for i in range(len(ret.__matrix)):
            for j in range(len(matrix.__matrix[i])):
                ret.__matrix[i][j] = ret.__matrix[i][j] + matrix.__matrix[i][j]
        return ret
sourceData1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
sourceData2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
matrix1 = Matrix(sourceData1)
matrix2 = Matrix(sourceData1)
print('матрица 1')
print(matrix1)
print('матрица 2')
print(matrix2)
print('сложение матрицы 1 и матрицы 2')
print(matrix1 + matrix2)