# 2. Из предложенного текстового файла (text18-16.txt) вывести на экран его содержимое,
# количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив все знаки пунктуации на знак «!».
with open("ТЕКСТ(PZ-11-2).txt", "r") as file:
    content = file.read()
uppercase_count = sum(1 for char in content if char.isupper())
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
content_punctuation = ''.join('!' if char in punctuation else char for char in content)
print(content)
print("Количество букв в верхнем регистре:", uppercase_count)
with open("новый_файл.txt", "w") as file:
    file.write(content_punctuation)