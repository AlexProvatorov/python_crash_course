#Создаю три словаря с данными о каждом юзере
aprovatorov = {
    'first_name': 'александр',
    'last_name': 'проваторов',
    'age': '21',
    'city': 'луганск',
    }
eprovatorov = {
    'first_name': 'евгений', 
    'last_name': 'проваторов', 
    'age': '17', 
    'city': 'красный луч',
    }
cstaritskaya = {
    'first_name': 'кристина', 
    'last_name': 'старицкая',
    'age': '22', 
    'city': 'луганск',
    }
#Сохраняем все словари в списке
people = [aprovatorov, eprovatorov, cstaritskaya]
#Перебор и вывод всей инфы о юзерах
for user in people:
    print("Имя: " + user['first_name'].title())
    print("Фамилия: " + user['last_name'].title())
    print("Возраст: " + user['age'].title())
    print("Город: " + user['city'].title() + "\n")
