"""
Фокусники без изменений: начните с программы из упражнения 8-10. Вызовите 
функцию make_great() и передайте ей копию списка имен фокусников. 
Поскольку исходный список остался неизменным, верните новый список и 
сохраните его в отдельном списке.и Вызовите функцию show_magicians()
с каждым списком, чтобы показать, что в одном списке остались исходные 
имена, а в другом к имени каждого фокусника добавилась приставка «Great».
"""

name_magicians = ['david blaine','steven frayne','criss enjel',]
great_name_magicians = []
#Функция извлекает имена из списка и выводит в правильном регистре
def show_magicians(names):
    print("\nСпискок имен: ")
    for name in names:
        print(name.title())
#Функция имена, добавляет "great" и сохраняет в пустой словарь
def make_great(names):
    for i in range(len(names)):
        names[i] = "great " + names[i]
        great_name_magicians.append(names[i])
    return names

make_great(name_magicians[:])

show_magicians(name_magicians)
show_magicians(great_name_magicians)