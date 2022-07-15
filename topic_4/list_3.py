#Создание числового списка
numbers = list(range(1,21))
print(numbers)
#Создаю список идущий через 3
even_numbers = list(range(3,31,3))
print(even_numbers)
#Список квадратов всех чисел от 1 до 10
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
#Простая статистика списка
print(min(squares))
print(max(squares))
print(sum(squares))
