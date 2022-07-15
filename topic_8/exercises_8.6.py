"""
Названия городов: напишите функцию city_country(), которая получает название города 
и страну. Функция должна возвращать строку в формате “Santiago, Chile”. Вызовите
свою функцию по крайней мере для трех пар «город—страна» и выведите возвращенное
значение.
"""

def city_country(city_name, country_name):
    message = city_name + ', ' + country_name + "."
    return message.title()

santiago = city_country('santiago', 'chile')
print(santiago)

moscow = city_country('moscow', 'russia')
print(moscow)

paris = city_country('paris', 'france')
print(paris)
