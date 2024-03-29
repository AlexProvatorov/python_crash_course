"""
Профиль: начните с копии программы user_profile.py. Создайте
собственный профиль вызовом build_profile(), укажите имя, 
фамилию и три другие пары «ключ—значение» для вашего описания.
"""

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    #Перебираем пары ключ-значение заданные юзером
    #Сохраняем в словарь
    for key, value in user_info.items():
        profile[key] = value
    return profile 

user_profile = build_profile(
    'alex','satan', location = 'lugansk',
    hobby = 'coding', lenguage = 'python'
    )

print(user_profile)