"""
Hello Admin: создайте список из пяти и более имен пользователей, 
включающий имя ‘admin’. Представьте, что вы пишете код, который выводит 
приветственное сообщение для каждого пользователя после его входа на 
сайт. Переберите элементы списка и выведите сообщение для каждого 
пользователя.
• Для пользователя с именем 'admin’ выведите особое сообщение — 
например: «Hello admin, would you like to see a status report?»
• В остальных случаях выводите универсальное приветствие — например: 
«Hello Eric, thank you for logging in again».
"""

users_name = ['criss', 'john', 'jack', 'tony', 'michael', 'admin',]

for user_name in users_name: 
    if 'admin' in user_name:
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user_name.title() + ", thank you for logging in again")
