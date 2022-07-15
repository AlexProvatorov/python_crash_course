"""
Большие футболки: измените функцию make_shirt(), чтобы футболки по умолчанию
имели размер L, и на них выводился текст «I love Python.». Создайте футболку 
с размером L и текстом по умолчанию, а также футболку любого размера с другим
текстом.
"""

def make_shirt(shirt_size = 'l', shirt_print = 'I love Python!'):
    print("Размер футболки: " + shirt_size.title() + ".")
    print("Принт на футболке: " + shirt_print.title() + "\n")

#по умолчанию
make_shirt()
#позиционные аргументы
make_shirt('m', 'just do it!')
#именованные аргументы
make_shirt(shirt_size = 'xxl', shirt_print = 'software engineer')