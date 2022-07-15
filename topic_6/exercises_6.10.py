"""
Любимые числа: измените программу из упражнения 6.2, чтобы для каждого
человека можно было хранить более одного любимого числа. Выведите имя 
каждого человека в списке и его любимые числа.
"""
favorit_numbers = {
    'alex': ['23','86',],
    'john': ['16', '44', '28',],
    'frank': ['48',],
    'boris': ['13', '666',],
    }
for name, numbers in favorit_numbers.items():
    print("\n" + name.title() + "'s favorite numbers: ")
    for number in numbers:
        print("\t" + number)