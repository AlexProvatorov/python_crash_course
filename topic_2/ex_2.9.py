# Любимое число: сохраните свое любимое число в переменной.
# Затем при помощи переменной создайте сообщение для вывода этого числа. Выведите это сообщение.

favorite_number = input("Введите ваше любимое число: ")
favorite_number = favorite_number.strip()
message = ("Ваше любимое число - " + str(favorite_number) + "!")

print(message)