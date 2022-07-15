"""
Города: напишите функцию describe_city(), которая получает названия 
города и страны. Функция должна выводить простое сообщение 
(например, «Reykjavik is in Iceland») . Задайте параметру страны 
значение по умолчанию . Вызовите свою функцию для трех разных городов, 
по крайней мере один из которых не находится в стране по умолчанию .
"""

def describe_city(city, country='usa'):
    if country != 'usa':
        print(city.title() + " is in " + country.title())
    else:
        print(city.title() + " is in " + country.upper())

describe_city('new york')
describe_city('miami')
describe_city('rostov', 'russia')
