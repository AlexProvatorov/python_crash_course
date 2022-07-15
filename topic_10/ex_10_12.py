"""

Сохраненное любимое число: объедините две программы из упражнения 10-11 в один
файл. Если число уже сохранено, сообщите его пользователю, а если нет —
запросите любимое число пользователя и сохраните в файле. Выполните программу
дважды, чтобы убедиться в том, что она работает.

"""
import json

file_name = 'favorite_number.json'
try:
    with open(file_name, 'r') as file_object:
        user_number = json.load(file_object)
except FileNotFoundError:
    user_number = input("Введите ваше любимое число: ")
    with open(file_name, 'w') as file_object:
        json.dump(user_number, file_object)
else:
    print("Я запомнил ваше любимое число: " + user_number + "!")