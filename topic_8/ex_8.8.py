"""
Пользовательские альбомы: начните с программы из упражнения 8-7. 
Напишите цикл while, в котором пользователь вводит исполнителя и 
название альбома. Затем в цикле вызывается функция make_album() для 
введенных пользователей и выводится созданный словарь. Не забудьте 
предусмотреть признак завершения в цикле while .
"""
def make_album(rock_band, album_name, total_tracks = ''):
    album = {'band': rock_band, 'name': album_name}
    if total_tracks:
        album['tracks'] = total_tracks
    return album

message_1 = "Введите название группы чтобы прододжить или 'q' для выхода: "
message_2 = "Введите название альбома чтобы прододжить или 'q' для выхода: "

while True:
    rock_band = input(message_1)
    if rock_band == 'q':
        break
    album_name = input(message_2)
    if album_name == 'q':
        break
    decision = input("Желаете ввести кол-во треков в альбоме(y/n)?")
    if decision == 'y':
        total_tracks = input("Введите кол-во треков в альбоме: ")
        album_info = make_album(rock_band, album_name, total_tracks)
    else:
        album_info = make_album(rock_band, album_name)
    print(album_info)