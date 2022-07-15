""" 
Срезы: добавьте в конец одной из программ, написанных в этой главе, фрагмент,
который делает следующее.
• Выводит сообщение «The first three items in the list are:», а затем использует срез для
вывода первых трех элементов из списка.
• Выводит сообщение «Three items from the middle of the list are:», а затем использует
срез для вывода первых трех элементов из середины списка.
• Выводит сообщение «The last three items in the list are:», а затем использует срез для
вывода последних трех элементов из списка.
"""

items = ['koffe', 'tea', 'caps', 'spun', 'knife', 'pan', 'artbook', 'flashcard', 'macbook', 'map',]
print("The first three items in the list are:")
for item in items[:3]:
    print(item)
print("Three items from the middle of the list are:")
for item in items[4:7]:
    print(item)
print("The last three items in the list are:")
for item in items[-3:]:
    print(item)