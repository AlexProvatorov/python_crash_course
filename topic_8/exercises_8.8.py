"""
Пользовательские альбомы: начните с программы из упражнения 8-7. 
Напишите цикл while, в котором пользователь вводит исполнителя и
название альбома. Затем в цикле вызывается функция make_album() 
для введенных пользователей и выводится созданный словарь. Не 
забудьте предусмотреть признак завершения в цикле while.
"""

def make_album(artist_name, album_name,):
    album = {'artist_n': artist_name, 'album_n': album_name,}
    return album

active = True
while active:
    print("\nВведите данные для заполнения словаря: ")
    art = input("Введит имя исполнителя: ")
    alb = input("Введите название альбома: ")
    
    album_info = make_album(art, alb)
    active = False 

print(album_info)
    