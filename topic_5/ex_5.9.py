"""
Без пользователей: добавьте в ex_5.8.py команду if, которая проверит, 
что список пользователей не пуст.
• Если список пуст, выведите сообщение: «We need to find some users!»
• Удалите из списка все имена пользователей и убедитесь в том, что 
программа выводит правильное сообщение.
"""

users_name = []

if users_name:
    for user_name in users_name: 
        if 'admin' in user_name:
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user_name.title() + ", thank you for logging in "
                  "again"
                 )
else:
    print("We need to find some users!")
