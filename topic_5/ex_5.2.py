"""
Больше условий: количество условий не ограничивается 10. Попробуйте 
написать другие условия и включить их в conditional_tests.py. Программа 
должна выдавать по крайней мере один истинный и один ложный результат 
для следующих видов проверок.
• Проверка равенства и неравенства строк.
• Проверки с использованием функции lower().
• Числовые проверки равенства и неравенства, условий «больше», «меньше»,
«больше или равно», «меньше или равно».
• Проверки с ключевым словом and и or.
• Проверка вхождения элемента в список.
• Проверка отсутствия элемента в списке
"""

motorcycle = 'Yamaha'

#Проверка равенства и неравенства строк
print("Это Yamaha?")
print(motorcycle == 'Yamaha')

print("Это Ducati?")
print(motorcycle == 'Ducati')

print("Это не Ducati?")
print(motorcycle != 'Ducati')

print("Это не Yamaha?")
print(motorcycle != 'Yamaha')

#Проверки с использованием функции lower()
print("Это yamaha?")
print(motorcycle.lower() == 'yamaha')

print("Это ducati?")
print(motorcycle.lower() == 'ducati')

#Числовые проверки равенства и неравенства чисел, условий: >, <, >=, <=
number_1 = 23
number_2 = 15

print("Первое число равно 23?")
print(number_1 == 23)

print("Второе число не равно 15?")
print(number_2 != 15)

print("Первое число больше второго?")
print(number_1 > number_2)

print("Первое число меньше второго?")
print(number_1 < number_2)

print("Первое число больше или равно второму?")
print(number_1 >= number_2)

print("Первое число меньше или равно второму?")
print(number_1 <= number_2)

#Проверки с ключевым словом and и or
print("Первое число равно 23 и второе равно 15?")
print(number_1 == 23 and number_2 == 15)

print("Первое число равно 22 или второе равно 14?")
print(number_1 == 22 or number_2 == 14)

#Проверка вхождения элемента в список
motorcycles = ['ducati', 'bmw', 'yamaha', 'kawasaki',]
print("BMW есть в списке мотоциклов?")
print('bmw' in motorcycles)

print("KTM есть в списке мотоциклов?")
print('ktm' in motorcycles)

#Проверка отсутствия элемента в списке
print("Indian отсутсвует в списке мотоциклов?")
print('indian' not in motorcycles)

print("Kawasaki отсутсвует в списке мотоциклов?")
print('kawasaki' not in motorcycles)