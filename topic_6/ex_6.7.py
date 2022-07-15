"""
Люди: начните с программы, написанной для упражнения 6-1 (с. 107). 
Создайте два новых словаря, представляющих разных людей, и сохраните все
три словаря в списке с именем people. Переберите элементы списка людей.
В процессе перебора выведите всю имеющуюся информацию о каждом человеке.
"""

user_0 = {
    'first_name': 'alex',
    'last_name': 'satan',
    'age': '22',
    'city': 'rostov',
    }

user_1 = {
    'first_name': 'max',
    'last_name': 'gordon',
    'age': '21',
    'city': 'moscow',
    }

user_2 = {
    'first_name': 'criss',
    'last_name': 'vector',
    'age': '22',
    'city': 'rostov',
    }

people = [user_0, user_1, user_2,]

print("Почетные юзеры сайта:\n")

for user in people:
    print("Имя: " + user['first_name'].title() + ".")
    print("Полное имя: " + user['first_name'].title() +
        " " + user['last_name'].title() + ".")
    print("Возраст: " + str(user['age']) + ".")
    print("Живет в городе " + user['city'].title() + ".\n")