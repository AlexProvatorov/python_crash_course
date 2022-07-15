"""
Фокусники: создайте список с именами фокусников. Передайте список 
функции show_magicians(), которая выводит имя каждого фокусника в
списке.

Назову show_names т.к. это сделает функцию универсальной для вывода
имен из любых списков!
"""

name_magicians = ['david blaine','steven frayne','criss enjel',]

#Функция извлекает имена из списка и выводит в правильном регистре
def show_names(names):
    print("Спискок имен: ")
    for name in names:
        print(name.title())

show_names(name_magicians)