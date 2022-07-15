"""
Все функции: придумайте информацию, которую можно было бы хранить в списке.
Например, создайте список гор, рек, стран, городов, языков… словом, чего угодно. 
Напишите программу, которая создает список элементов, а затем вызывает каждую функцию,
упоминавшуюся в этой главе, хотя бы один раз.
"""

countries = ['canada', 'czechia', 'germany', 'north korea', 'japan',]
print("Изначальный список стран:")
print(countries)

print("\nИзменим один элемент списка:")
countries[1] = 'usa'
print(countries)

print("\nДобавление новых элементов в конец, середину и начало:")
countries.append('italy')
countries.insert(0, 'france')
countries.insert(3, 'poland')
print(countries)

print("\nУдалим первый элемент:")
del countries[0]
print(countries)

print("\nУдалим с сохранение 4 элемент списка, выведем его:")
popped_countries = countries.pop(3)
print(countries)
print(popped_countries)

print("\nУдалим польшу из списка:")
countries.remove('poland')
print(countries)

print("\nСортируем для вывода без изменения списка, через sorted():")
print(sorted(countries))
print(countries)

print("\nСохраним список в обратном алфавитном порядке, через sort():")
countries.sort(reverse=True)
print(countries)

print("\nВыведем в алфавитном порядке через reverse():")
countries.reverse()
print(countries)

print("\nКол-во элементов в списке:")
print(len(countries))