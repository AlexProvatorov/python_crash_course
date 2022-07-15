"""
Сообщения: начните со списка, использованного в упражнении 3-1, но вместо вывода
имени каждого человека выведите сообщение. Основной текст всех сообщений должен
быть одинаковым, но каждое сообщение должно включать имя адресата.
"""

names = ['alex', 'criss', 'jack', 'john', 'max',]
message_1 = "Рад приветствовать тебя, "
message_2 = "! Приятно снова видеть тебя в наших рядах!"

print(message_1 + names[0].title() + message_2)
print(message_1 + names[1].title() + message_2)
print(message_1 + names[2].title() + message_2)
print(message_1 + names[3].title() + message_2)
print(message_1 + names[-1].title() + message_2)