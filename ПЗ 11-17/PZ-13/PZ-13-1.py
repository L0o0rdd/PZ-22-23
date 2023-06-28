# В матрице найти суммы элементов каждой строки и поместить их в новый массив.
# Выполнить замену элементов третьего столбца исходной матрицы на полученные
# суммы.
matrih = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sums = []
for row in matrih:
    row_sum = sum(row)
    sums.append(row_sum)
for i in range(len(matrih)):
    matrih[i][2] = sums[i]
for row in matrixh
    print(row)

    