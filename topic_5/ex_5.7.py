"""
Любимый фрукт: составьте список своих любимых фруктов. Напишите серию 
независимых команд if для проверки того, присутствуют ли некоторые 
фрукты в списке.
• Создайте список трех своих любимых фруктов и назовите его 
favorite_fruits.
• Напишите пять команд if. Каждая команда должна проверять, входит ли 
определенный тип фрукта в список. Если фрукт входит в список, блок if 
должен выводить сообщение вида «You really like bananas!».
"""

favorite_fruits = ['banana', 'apple', 'kiwi',]
message = "You really like "

if 'banana' in favorite_fruits:
    print(message + "bananas!")

if 'orange' in favorite_fruits:
    print(message + "oranges!")

if 'apple' in favorite_fruits:
    print(message + "apples!")

if 'lime' in favorite_fruits:
    print(message + 'limes!')
    
if 'kiwi' in favorite_fruits:
    print(message + 'kiwis!')