"""
Проверка условий: напишите последовательность условий. Выведите описание
каждой проверки и ваш прогноз относительно ее результата. Код должен 
выглядеть примерно так:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Внимательно просмотрите результаты. Убедитесь в том, что вы понимаете,
почему результат каждой строки равен True или False.
• Создайте как минимум 10 условий. Не менее 5 должны давать результат 
True, а не ­менее 5 других — результат False.
"""

number_1 = 23
number_2 = 15

print("number_1 равен 23? Предсказываю True!")
print(number_1 == 23)

print("\nnumber_1 равен 62? Предсказываю False!")
print(number_1 == 62)

print("\nnumber_1 не равен 62? Предсказываю True!")
print(number_1 != 62)

print("\nnumber_1 не равен 23? Предсказываю False!")
print(number_1 != 23)

print("\nnumber_1 == 23 and number_2 == 15? Предсказываю True!")
print(number_1 == 23 and number_2 == 15)

print("\nnumber_1 == 22 and number_2 == 15? Предсказываю False!")
print(number_1 == 22 and number_2 == 15)

print("\nnumber_1 != 22 and number_2 != 14? Предсказываю True!")
print(number_1 != 22 and number_2 != 14)

print("\nnumber_1 != 23 and number_2 != 15? Предсказываю False!")
print(number_1 != 23 and number_2 != 15)

print("\nnumber_1 == 22 or number_2 == 15? Предсказываю True!")
print(number_1 == 22 or number_2 == 15)

print("\nnumber_1 == 22 or number_2 != 15? Предсказываю False!")
print(number_1 == 22 or number_2 != 15)