"""
Больше гостей: вы решили купить обеденный стол большего размера. Дополнительные
места позволяют пригласить на обед еще трех гостей.
• Начните с программы из упражнения 3-4 или 3-5. Добавьте в конец программы команду print, которая 
выводит сообщение о расширении списка гостей.
• Добавьте вызов insert() для добавления одного гостя в начало списка.
• Добавьте вызов insert() для добавления одного гостя в середину списка.
• Добавьте вызов append() для добавления одного гостя в конец списка.
• Выведите новый набор сообщений с приглашениями – по одному для каждого участника, входящего в список.
"""

visitors = ['elon musk', 'mark zuckerberg', 'steve jobs', 'pavel durov', 'bill gates',]
message = "! Обязательно приходи сегодня на обед. Мероприятие обещает быть веселым!\n"

print(visitors[0].title() + message)
print(visitors[3].title() + message)
print(visitors[1].title() + message)

print("Список гостей расширяется!\n")

visitors.insert(0, 'linus torvalds')
visitors.insert(3, 'john carmack')
visitors.append('guido van rossum')

print(visitors[0].title() + message)
print(visitors[1].title() + message)
print(visitors[2].title() + message)
print(visitors[3].title() + message)
print(visitors[4].title() + message)
print(visitors[5].title() + message)
print(visitors[6].title() + message)
print(visitors[7].title() + message)
