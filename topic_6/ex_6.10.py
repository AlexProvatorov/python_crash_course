"""
Любимые числа: измените программу из упражнения 6-2 (с. 107), чтобы для 
каждого человека можно было хранить более одного любимого числа. 
Выведите имя каждого человека в списке и его любимые числа.
"""

favorite_numbers = {
    'alex': [23, 15, 99],
    'criss': [10, 39],
    'john': [33, 48, 69, 124],
    'michael': [69, 24],
    'bob': [7, 14]
    }

message = "Любимые числа "

for name, numbers in favorite_numbers.items():
    print("\n" + message + name.title() + ":")
    for number in numbers:
        print(str(number)) 