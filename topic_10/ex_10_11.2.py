"""

Любимое число: напишите программу, которая запрашивает у пользователя его
любимое число. Воспользуйтесь функцией json.dump() для сохранения этого числа в
файле. Напишите другую программу, которая читает это значение и выводит
сообщение: «Я знаю ваше любимое число! Это _____».

"""
import json

file_name = 'favorite_number.json'
with open(file_name, 'r') as file_object:
    user_number = json.load(file_object)
print("Я знаю ваше любимое число! Это " + user_number + "!")