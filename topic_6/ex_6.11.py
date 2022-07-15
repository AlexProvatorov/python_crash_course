"""
Города: создайте словарь с именем cities. Используйте названия трех 
городов в качестве ключей словаря. Создайте словарь с информацией о 
каждом городе; включите в него страну, в которой расположен город, 
примерную численность населения и один примечательный факт, относящийся 
к этому городу. Ключи словаря каждого города должны называться country, 
population и fact. Выведите название каждого города и всю сохраненную
информацию о нем.
"""

cities = {
    'lugansk': {
        'country': 'ukraine',
        'population': '403 938',
        'fact': 'Ранее назывался Ворошиловград.',
        },
    'rostov': {
        'country': 'russia',
        'population': '1 137 704',
        'fact': 'В городе присутсвуют 106 национальностей.',
        },
    'moscow': {
        'country': 'russia',
        'population': '12 655 050',
        'fact': 'Авиационный узел один из самых крупных авиаузлов в мире.',
        },
    }

for city_name, city_info in cities.items():
    print("\nНазвание города: " + city_name.title())
    print("Страна: " + city_info['country'].title())
    print("Численность населения: " + city_info['population'])
    print("Факт: " + city_info['fact'])