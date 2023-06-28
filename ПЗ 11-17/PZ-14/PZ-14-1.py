# Из исходного текстового файла (price.txt) выбрать все цены. Посчитать количество
# полученных элементов.
with open('price.txt', 'r') as file:
    content = file.read()
import re
pat = r'\d+ руб\. \d+ коп\.'
prices = re.findall(pat, content)#Функция findall находит все соответствующие совпадения и возвращает их в виде списка prices. Затем мы используем функцию len для подсчета количества цен в списке и выводим результат.
count = len(prices)
print(f'Количество цен: {count}')