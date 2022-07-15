"""

Гость: напишите программу, которая запрашивает у пользователя его имя. 
Введенный ответ сохраняется в файле с именем guest.txt

"""
file_path = '/home/alex_satan/my_code/guest.txt'

with open(file_path, 'w') as file_object:
    guest_name = input("Введите ваше имя: ")
    file_object.write(guest_name.title())