#Цвета 3: преобразуйте цепочку if-else из упражнения 5-4 в цепочку if-elif-else.
#Если переменная содержит значение 'green’, выведите сообщение о том, что игрок
#только что заработал 5 очков.
#Если переменная содержит значение 'yellow’, выведите сообщение о том, что игрок
#только что заработал 10 очков.
#Если переменная содержит значение 'red’, выведите сообщение о том, что игрок только что заработал 15 очков.
#Напишите три версии программы и проследите за тем, чтобы для каждого цвета пришельца выводилось соответствующее сообщение.
alien_color = 'green'
if 'green' in alien_color:
    print('Вы заработали 5 очков!')
elif 'yellow' in alien_color:
    print('Вы заработали 10 очков!')
elif 'red' in alien_color:
    print('Вы заработали 15 очков!')

alien_color = 'yellow'
if 'green' in alien_color:
    print('Вы заработали 5 очков!')
elif 'yellow' in alien_color:
    print('Вы заработали 10 очков!')
elif 'red' in alien_color:
    print('Вы заработали 15 очков!')

alien_color = 'red'
if 'green' in alien_color:
    print('Вы заработали 5 очков!')
elif 'yellow' in alien_color:
    print('Вы заработали 10 очков!')
elif 'red' in alien_color:
    print('Вы заработали 15 очков!')

