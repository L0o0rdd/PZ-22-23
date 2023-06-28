# Составить генератор (yield), который переведет символы строки из нижнего
# регистра в верхний
def generator(string):
    for char in string:
        if char.islower():
            yield char.upper()
        else:
            yield char

string = "ПУпуПУпупупупуупупПУ"
result = ''.join(generator(string))

print(result)