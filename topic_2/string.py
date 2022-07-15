#Работа со строкой
#Регистр
user_name = input("Введите имя пользователя:  ")
print(user_name.title())
print(user_name.upper())
print(user_name.lower())

#Конкатенация регистр и пропуски
first_name = input("Введите Ваше имя: ")
first_name = first_name.strip().title()
lust_name = input("Введите вашу фамилию: ")
lust_name = lust_name.strip().title()
full_name = first_name + " " + lust_name
message = ("Здравствуй, "+ full_name+". Рад видеть, что ты занят полезным делом.")
print(message)

#Табуляция и перенос строки
print("Языки программирования: \n\tPython, \n\tJavaScript, \n\tC.")

#Функция str() и предотвращение ошибок
number = 6
print("Я учился "+str(number)+" лет, и только сейчас понял, что это полная лажа. Я не хочу так жить!")

