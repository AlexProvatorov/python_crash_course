"""
Профиль: начните с копии программы user_profile.py. Создайте собственный
профиль вызовом build_profile(), укажите имя, фамилию и три другие пары
«ключ—значение» для вашего описания.
"""

def build_profile(first, last, **user_info):
    user_profile = {}
    user_profile['first_name'] = first
    user_profile['last_name'] = last
    for key, value in user_info.items():
        user_profile[key] = value
    return user_profile

admin = build_profile('alex', 'satan', location='lugansk', profession='it')
            
print(admin)