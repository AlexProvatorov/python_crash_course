"""
Альбом: напишите функцию make_album(), которая строит словарь с описанием 
музыкального альбома. Функция должна получать имя исполнителя и название 
альбома и возвращать словарь, содержащий эти два вида информации. 
Используйте функцию для создания трех словарей, представляющих разные 
альбомы. Выведите все возвращаемые значения, чтобы показать, что 
информация правильно сохраняется во всех трех словарях.
Добавьте в make_album() дополнительный параметр для сохранения количества дорожек
в альбоме. Если в строку вызова включено значение количества дорожек, добавьте 
это значение в словарь альбома. Создайте как минимум один новый вызов функции 
с передачей количества дорожек в альбоме.
"""

def make_album(artist_name, album_name, num_tracks = ''):
    if num_tracks:
        album = {'artist_n': artist_name, 'album_n': album_name, 'n_tracks': num_tracks,}
    else:
        album = {'artist_n': artist_name, 'album_n': album_name,}
    return album

acdc = make_album('ACDC', 'Back in Black')
rammstein = make_album('Rammstein', 'Mutter', num_tracks = 12)
skillet = make_album('Skillet', 'Rise')

print(acdc)
print(rammstein)
print(skillet)
