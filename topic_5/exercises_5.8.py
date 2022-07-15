#авторизация пользователей и админа
users = ['alex', 'criss', 'admin', 'ruslan', 'max']

for user in users:
    if 'admin' in user:
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello "+user+", thank you for logging in again.")
