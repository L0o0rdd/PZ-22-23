# В матрице найти сумму элементов второй половины матрицы.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rows = len(matrix)
cols = len(matrix[0])
start_index = cols // 2
sum_second_half = 0
for i in range(rows):
    for j in range(start_index, cols):
        sum_second_half += matrix[i][j]
print("Сумма элементов во второй половине матрицы:", sum_second_half)