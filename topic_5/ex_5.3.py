"""
Цвета 1: представьте, что в вашей компьютерной игре только что был 
подбит корабль пришельцев. Создайте переменную с именем alien_color и 
присвойте ей значение ‘green’, ‘yellow’ или ‘red’.
• Напишите команду if для проверки того, что переменная содержит 
значение ‘green’. Если условие истинно, выведите сообщение о том, что 
игрок только что заработал 5 очков.
• Напишите одну версию программы, в которой условие if выполняется, и 
другую версию, в которой оно не выполняется. (Во второй версии никакое 
сообщение выводиться не должно.)
"""
#Условие выполняется
alien_color = 'green'
if alien_color == 'green':
    print("Вы заработали 5 очков!")

#Условие не выполняется
alien_color = 'red'
if alien_color == 'green':
    print("Вы заработали 5 очков!")