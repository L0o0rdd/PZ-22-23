# В последовательности на n целых чисел умножить все элементы на первый
# элемент
sisl = [3, 5, 2, 8, 3]
for i in range(len(sisl)):
    sisl[i] = sisl[i] * sisl[0]
print(sisl)