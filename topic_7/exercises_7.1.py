"""
Прокат машин: напишите программу, которая спрашивает у пользователя, какую машину он хотел бы
взять напрокат. Выведите сообщение с введенными данными (например, “Let me see if I can find
you a Subaru”).

"""

car = input("Какую машину желаете взять на прокат? \n")
message = 'Давайте посмотрим, смогу ли я найти для вас '

print(message + car + "!")