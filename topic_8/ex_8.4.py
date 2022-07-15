"""
Большие футболки: измените функцию make_shirt(), чтобы футболки по 
умолчанию имели размер L, и на них выводился текст «I love Python.».
Создайте футболку с размером L и текстом по умолчанию, а также футболку
любого размера с другим текстом .
"""

def make_shirt(size='l', text='i love python'):
    print("Размер футболки: " + size.upper() + ".")
    print("Надпись на футболке: " + text.title() + ".\n")

#по умолчанию
make_shirt()
#позиционно
make_shirt('m', 'dust do it')
#именованно
make_shirt(text='i lowe squirrel', size='s')