"""
Любимая книга: напишите функцию favorite_book(), которая получает один
параметр title. Функция должна выводить сообщение вида «One of my 
favorite books is Alice in Wonderland». Вызовите функцию и убедитесь в 
том, что название книги правильно передается как аргумент при вызове 
функции.
"""

def favorite_book(book_name):
    """Выводит сообщение о любимой книге"""
    print("Одно из моих любимых поизведений это книга " + 
           book_name.title() + ".")

favorite_book('вокруг света за 80 дней')
favorite_book('ведьмак')