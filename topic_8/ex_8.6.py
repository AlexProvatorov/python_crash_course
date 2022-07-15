"""
Названия городов: напишите функцию city_country(), которая получает 
название города и страну. Функция должна возвращать строку в формате 
“Santiago, Chile”. Вызовите свою функцию по крайней мере для трех пар 
«город—страна» и выведите возвращенное значение.
"""

def city_country(city_name, country_name):
    full_info = city_name + ", " + country_name + "."
    return full_info.title()

chile = city_country('santiago', 'chile')
russia = city_country('moscow', 'russia')
france = city_country('paris', 'france')

capitals = [chile, russia, france]

for capital in capitals:
    print(capital)