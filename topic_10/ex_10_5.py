"""

Опрос: напишите цикл while, в котором программа спрашивает у пользователя,
почему ему нравится программировать. Каждый раз, когда пользователь вводит
очередную причину, сохраните текст его ответа в файле.

"""
file_path = 'reasons.txt'

message = "Введите причину по которой вы любите кодить\n"
message += "('q' для выхода): "

while True:
    user_reason = input(message)
    if user_reason == 'q':
        break
    else:
        with open(file_path, 'a') as file_object:
            file_object.write(user_reason + "\n")