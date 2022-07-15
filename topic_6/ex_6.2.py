"""
Любимые числа: используйте словарь для хранения любимых чисел. Возьмите
пять имен и используйте их как ключи словаря. Придумайте любимое число 
для каждого человека и сохраните его как значение в словаре. Выведите
имя каждого человека и его любимое число. Чтобы задача стала более
интересной, опросите нескольких друзей и соберите реальные данные для 
своей программы.
"""

favorite_numbers = {
    'alex': '23',
    'criss': '10',
    'john': '33',
    'michael': '69',
    'bob': '7',
    }

message = "Любимое число "

print(message + "Alex это " + str(favorite_numbers['alex']) + ".\n")
print(message + "Criss это " + str(favorite_numbers['criss']) + ".\n")
print(message + "John это " + str(favorite_numbers['john']) + ".\n")
print(message + "Michael это " + str(favorite_numbers['michael']) + ".\n")
print(message + "Bob это " + str(favorite_numbers['bob']) + ".\n")
