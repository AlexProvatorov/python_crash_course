"""
Великие фокусники: начните с копии вашей программы из упражнения 8-9.
Напишите функцию make_great(), которая изменяет список фокусников, 
добавляя к имени каждого фокусника приставку «Great». Вызовите функцию
show_magicians() и убедитесь в том, что список был успешно изменен.
"""

name_magicians = ['david blaine','steven frayne','criss enjel',]

#Функция извлекает имена из списка и выводит в правильном регистре
def show_magicians(names):
    print("Спискок имен: ")
    for name in names:
        print(name.title())

def make_great(names):
    for i in range(len(names)):
        names[i] = "great " + names[i]
    return names

make_great(name_magicians)
show_magicians(name_magicians)

