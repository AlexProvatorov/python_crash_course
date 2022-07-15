"""
Города: напишите функцию describe_city(), которая получает названия города 
и страны. Функция должна выводить простое сообщение (например, «Reykjavik 
is in Iceland»). Задайте параметру страны значение по умолчанию. Вызовите 
свою функцию для трех разных городов, по крайней мере один из которых не 
находится в стране по умолчанию.
"""

def describe_city(city_name, country_name = 'ukraine'):
    print(city_name.title() + " is in " + country_name.title() + ".")

describe_city('kiev')
describe_city('moscov', 'russia')
describe_city('rostov', 'russia')
