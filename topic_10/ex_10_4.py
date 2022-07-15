"""

Гостевая книга: напишите цикл while, который в цикле запрашивает у пользователей
имена. При вводе каждого имени выведите на экран приветствие и добавьте строку с
сообщением в файл с именем guest_book.txt. Проследите за тем, чтобы каждое
сообщение размещалось в отдельной строке файла.

"""
file_path = '/home/alex_satan/my_code/guest_book.txt'

message = "Введите имя пользователя\n"
message += "('q' для завершения работы): "

while True:
    user_name = input(message)
    if user_name == 'q':
        break
    else:
        hello_user = "Hello, " + user_name.title() + "!"
        print(hello_user)
    with open(file_path, 'a') as file_object:
        file_object.write(hello_user + "\n")