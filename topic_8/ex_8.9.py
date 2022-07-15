"""
Фокусники: создайте список с именами фокусников . Передайте список
функции show_magicians(), которая выводит имя каждого фокусника в
списке.
"""

def show_magicians(magicians_names):
    for magician_name in magicians_names:
        print(magician_name.title())

magicians = ['devid blaine', 'garry gudini', 'steven frayne']

show_magicians(magicians)