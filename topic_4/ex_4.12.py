"""
Больше циклов: во всех версиях foods.py из этого раздела мы избегали использования
цикла for при выводе для экономии места. Выберите версию foods.py и напишите два цикла
for для вывода каждого списка.
"""

my_foods = ['pizza', 'falafel', 'carrot cake',]
print("My favorite foods are:")
for food in my_foods:
    print(food.title())
print("\nMy favorite reverse foods are:")
my_foods.reverse()
for food in my_foods:
    print(food.title())

