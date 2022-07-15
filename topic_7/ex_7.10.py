"""
Отпуск мечты: напишите программу, которая опрашивает пользователей, где 
бы они хотели провести отпуск . Включите блок кода для вывода 
результатов опроса 
"""

print("\n-----------Начнем опрос!-----------\n")

users_pool = {}

while True:
    name_user = input("Введите ваше имя: ")
    name_user = name_user.lower().strip()

    pool_answer = input("Введите место, где бы вы хотели провести отпуск: ")
    pool_answer = pool_answer.lower().strip()

    users_pool[name_user] = pool_answer

    user_choise = input("\nЖелаете продолжить опрос(Yes/no): ")
    user_choise = user_choise.lower()
    if user_choise == 'no':
        break
    elif user_choise == 'yes':
        continue
    else:
        print("Введена неверная команда! Опрос будет завершен!")
        break

print("\n-----------Результаты опроса!-----------\n")

for name, answer in users_pool.items():
    print(name.title() + " хочет отдохнуть в/на " + answer.title() + ".")
    
