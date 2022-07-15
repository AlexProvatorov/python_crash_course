"""
Сэндвичи: создайте список с именем sandwich_orders, заполните его 
названиями различных видов сэндвичей. Создайте пустой список с именем 
finished_sandwiches. В цикле переберите элементы первого списка и 
выведите сообщение для каждого элемента (например, «I made your tuna 
sandwich»). После этого каждый сэндвич из первого списка перемещается в
список finished_sandwiches. После того как все элементы первого списка
будут обработаны, выведите сообщение с перечислением всех изготовленных
сэндвичей.
"""

sandwich_orders = ['екста', 'веган', 'британ',]
finished_sandwiches = []

print("Начинаю готовить сэндвичи!\n")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("Я сделал тебе " + sandwich + " сендвич!")
    finished_sandwiches.append(sandwich)

print("\nЯ приготовил тебе: ")

for finished_sandwich in finished_sandwiches:
    print("\t" + finished_sandwich.title() + " сэндвич")
