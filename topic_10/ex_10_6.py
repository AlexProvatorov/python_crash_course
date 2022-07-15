"""

Сложение: при вводе числовых данных часто встречается типичная проблема: поль-
зователь вводит текст вместо чисел. При попытке преобразовать данные в int
происходит исключение ValueError. Напишите программу, которая запрашивает два
числа, складывает их и выводит результат. Перехватите исключение ValueError,
если какое-либо из входных значений не является числом, и выведите удобное
сообщение об ошибке. Протестируйте свою программу: сначала введите два числа,
а потом введите текст вместо одного из чисел.

"""
#Простой калькулятор для сложения чисел.
print("Введите два числа и я выполню их сложение.")
print("Введите 'q' для выхода.")

number_1 = input("Введите первое число: ")
number_2 = input("Введите второе число: ")
try:
    answer = float(number_1) + float(number_2)
except ValueError:
    print("Ошибка! Программа не может складывать текст!")
else:
    print("Ответ: " + str(answer))