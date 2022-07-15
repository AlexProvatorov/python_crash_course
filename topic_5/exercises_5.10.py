#Проверка наличия имени пользователя
current_users = ['alex', 'ban', 'john', 'max', 'sam']
new_users = ['criss', 'metty', 'alex', 'bruce', 'max']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Имя "+new_user.title()+ " уже используется. Пожалуйста введите другое имя.")
    else:
        print("Имя "+new_user.title()+" доступно для регистрации.")