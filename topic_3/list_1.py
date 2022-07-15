#Создание списка
weapons = ['AK', 'AR', 'HK', 'FN']
print(weapons)

#Обращение к элементам списка
print(weapons[1])
print(weapons[-1])

#Использование элементов списка
print("Моя любимая оружейная платформа, это "+weapons[0]+".")

#Изменение элеметов списка
weapons[3] = 'Glock'
print(weapons[3])

#Добавление элемета
weapons.append('Colt')
weapons.append(input("Введите новый элемент списка: "))
print(weapons)

#Вставка элемента 
weapons.insert(0, 'Beneli')
print(weapons)

#Удаление элемента
del weapons[0]
print(weapons)

weapons_1 = weapons.pop()
print(weapons_1)

weapons_dell = 'AR'
weapons.remove(weapons_dell)
print(weapons)
print(weapons_dell)

#Сортировка постоянная
weapons.sort()
print(weapons)
weapons.sort(reverse=True)
print(weapons)
#Сортировка временная
print("Это оригинальный порядок:")
print(weapons)
print("Это временная сортировка:")
print(sorted(weapons))
print("И снова оригинальная сортировка:")
print(weapons)
print("И вновь временная сортировка в обратном порядке:")
print(sorted(weapons, reverse=True))
#Вывод списка в обратном порядке
weapons.reverse()
print(weapons)
#Подсчет элеметов списка в терминал
len(weapons)