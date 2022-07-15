#Моя пицца, твоя пицца: начните с программы из упражнения 4-1. Создайте копию
#списка с видами пиццы, присвойте ему имя friend_pizzas. Затем сделайте следующее.
pizzas = ['дары моря','три сыра','греция']
friend_pizzas = pizzas[:]
#Добавьте новую пиццу в исходный список.
pizzas.append('пепперони')
#Добавьте другую пиццу в список friend_pizzas.
friend_pizzas.append('маргарита')
#Докажите, что в программе существуют два разных списка. Выведите сообщение «My
#favorite pizzas are:», а затем первый список в цикле for. 
print("My favorite pizzas are: ")
for pizza in pizzas[0:]:
    print(pizza.title())
# Выведите сообщение «My friend’s favorite pizzas are:», а затем второй список в цикле 
# for. Убедитесь в том, что каждая новая пицца находится в соответствующем списке.
print("\nMy friend’s favorite pizzas are: ")
for pizza in friend_pizzas[0:]:
    print(pizza.title())