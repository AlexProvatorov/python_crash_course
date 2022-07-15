"""
Без пастрами: используя список sandwich_orders из упражнения 7-8, проследите за
тем, чтобы значение ‘pastrami’ встречалось в списке как минимум три раза. Добавьте 
в начало программы код для вывода сообщения о том, что пастрами больше нет, и напишите
цикл while для удаления всех вхождений ‘pastrami’ из sandwich_orders. Убедитесь в том, 
что в finished_sandwiches значение ‘pastrami’ не встречается ни одного раза.
"""

sandwich_orders = ['чикен сендвич','веган сэндвич','чикен сендвич','супер сэндвич','дабл сэндвич','чикен сендвич']
finished_sandwiches = []

print("\nЧикен сендвича больше нет!")

while 'чикен сендвич' in sandwich_orders:
    sandwich_orders.remove('чикен сендвич')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("Я сделал тебе", sandwich.title() + "!")
    finished_sandwiches.append(sandwich)

print("\nВсе изготовленные сендвичи:")

for sandwich in finished_sandwiches:
    print(sandwich.title())
