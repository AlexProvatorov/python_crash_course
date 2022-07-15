#Создаем два списка из проверенных и непроверенных юзеров

unconfirmed_users = ['alex', 'max', 'john',]
confirmed_users = []

#Перебераем каждого юзера с конца выводим имя по мере проверки
#Добавляем проверенных юзеров в список проверенных

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Проверяемый юзер: " + current_user.title())
    confirmed_users.append(current_user)

#Выводим список проверенных юзеров

print("\nСписок проверенных юзеров: ")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())

