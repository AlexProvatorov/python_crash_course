"""
Реки: создайте словарь с тремя большими реками и странами, по которым
протекает каждая река. Одна из возможных пар «ключ—значение» — ‘nile’: 
‘egypt’.
• Используйте цикл для вывода сообщения с упоминанием реки и страны — 
например, «The Nile runs through Egypt.»
• Используйте цикл для вывода названия каждой реки, включенной в 
словарь.
• Используйте цикл для вывода названия каждой страны, включенной в 
словарь.
"""

rivers = {
    'nile': 'egypt',
    'don': 'russia',
    'amazon': 'usa',
    }

for river, country in rivers.items():
    if country.lower() == 'usa':
        print("The " + river.title() + " runs through " + country.upper() + ".")
    else:
        print("The " + river.title() + " runs through " + country.title() + ".")