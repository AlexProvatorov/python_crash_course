"""
Моя пицца, твоя пицца: начните с программы из упражнения 4-1. Создайте копию
списка с видами пиццы, присвойте ему имя friend_pizzas. Затем сделайте следующее.
• Добавьте новую пиццу в исходный список.
• Добавьте другую пиццу в список friend_pizzas.
• Докажите, что в программе существуют два разных списка. Выведите сообщение «My
favorite pizzas are:», а затем первый список в цикле for. Выведите сообщение «My
friend’s favorite pizzas are:», а затем второй список в цикле for. Убедитесь в том, что
каждая новая пицца находится в соответствующем списке.
"""

pizzas = ['three cheeses', 'pepperoni', 'hawaiian',]
friend_pizzas = pizzas[:]
pizzas.append('italika')
friend_pizzas.append('extra hot')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())
print("\nMy friend’s favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())
