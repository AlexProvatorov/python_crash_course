"""
Цвета 3: преобразуйте цепочку if-else из упражнения 5-4 в цепочку 
if-elif-else.
• Если переменная содержит значение 'green’, выведите сообщение о том, 
что игрок только что заработал 5 очков.
• Если переменная содержит значение 'yellow’, выведите сообщение о том, 
что игрок только что заработал 10 очков.
• Если переменная содержит значение 'red’, выведите сообщение о том, что
игрок только что заработал 15 очков.
• Напишите три версии программы и проследите за тем, чтобы для каждого 
цвета пришельца выводилось соответствующее сообщение.

Пошли нахер! Не буду я дублировать прогу 3 раза! Это скучно! Вот моя
"мини-игра".
"""

alien_color = 'white'
players_choice = input(
    "Прямо по курсу три корабля пришельцев!\nКакой"
    " корабль атаковать первым, Капитан?\nВарианты"
    ":\n1)Корабль слева;\n2)Корабль справа;\n3)Кор"
    "абль прямо по курсу;\nВведите номер команды: "
)

if players_choice == '1':
    alien_color = 'green'
elif players_choice == '2':
    alien_color = 'yellow'
elif players_choice == '3':
    alien_color = 'red'
else:
    print("Неверная команда! Экипаж поднял бунт!")

if alien_color == 'green':
    print("Вы заработали 5 очков!")
elif alien_color == 'yellow':
    print("Вы заработали 10 очков!")
elif alien_color == 'red':
    print("Вы заработали 15 очков!")
else:
    print("Ваш корабль был уничтожен! Ваши кишки обречены болтаться в космосе!")
