"""
Футболка: напишите функцию make_shirt(), которая получает размер 
футболки и текст, который должен быть напечатан на ней. Функция должна 
выводить сообщение с размером и текстом. Вызовите функцию с 
использованием позиционных аргументов . Вызовите функцию во второй раз 
с использованием именованных аргументов. 
"""

def make_shirt(size, text):
    print("Размер футболки: " + size.upper() + ".")
    print("Надпись на футболке: " + text.title() + ".\n")

#Позиционный аргумент
make_shirt('m', 'dust do it')
#Именованный аргумент
make_shirt(text='dust do it', size='xl')



