"""
Отпуск мечты: напишите программу, которая опрашивает пользователей, где бы они
хотели провести отпуск. Включите блок кода для вывода результатов опроса.
"""

responses = {}

polling_active = True

while polling_active:
    name = input("Как вас зовут? ")
    response = input("Где бы вы хотели провести отпуск? ")

    responses[name] = response

    repeat = input("Желаете продолжить опрос? (да/нет) ")
    if repeat == 'нет':
        polling_active = False
    elif repeat == 'да':
        continue

print("\n----------Pool Results----------")
for name, response in responses.items():
    print(name.title() + " хотел бы провести отпуск в " + response.title())
