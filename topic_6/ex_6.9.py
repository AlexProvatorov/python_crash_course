"""
Любимые места: создайте словарь с именем favorite_places. Придумайте 
названия трех мест, которые станут ключами словаря, и сохраните для 
каждого человека от одного до трех любимых мест. Чтобы задача стала 
более интересной, опросите нескольких друзей и соберите реальные данные
для своей программы. Переберите данные в словаре, выведите имя каждого 
человека и его любимые места.
"""

favorite_places = {
    'coffe house': ['criss', 'alex', 'oleg'],
    'hurma': ['alex', 'denis'],
    'top coffe': ['denis', 'oleg'],
    }

for place, names in favorite_places.items():
    print("\n" + place.title() + " любимое заведение для:")
    for name in names:
        print("\t" + name.title())