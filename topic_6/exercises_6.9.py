"""
Любимые места: создайте словарь с именем favorite_places. Придумайте трех людей, 
которые станут ключами словаря, и сохраните для каждого человека от одного до
трех любимых мест. Переберите данные в словаре, выведите имя каждого человека 
и его любимые места.
"""

favorite_places = {
    'alex': ['forest', 'river'],
    'john': ['city', 'river', 'fores'],
    'bob': ['forest',],
    }
#Используем перебор циклом и функию items для вывода keys(name), 
# чтобы вывести список - нужен еще один перебор циклом значения 
# values(places)  
for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places: ")
    for place in places:
        print(place.title())