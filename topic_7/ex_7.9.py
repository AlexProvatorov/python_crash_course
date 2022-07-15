"""
Без пастрами: используя список sandwich_orders из упражнения 7-8, 
проследите за тем, чтобы значение ‘pastrami’ встречалось в списке как 
минимум три раза . Добавьте в начало программы код для вывода сообщения
о том, что пастрами больше нет, и напишите цикл while для удаления всех
вхождений ‘pastrami’ из sandwich_orders . Убедитесь в том, что в 
finished_sandwiches значение ‘pastrami’ не встречается ни одного раза.
"""

sandwich_orders = ['екста', 'пастрами', 'веган', 'пастрами', 'британ',
                   'пастрами',]
finished_sandwiches = []

print("Начинаю готовить сэндвичи!\n")
print("Пастрами закончился!\n")

while 'пастрами' in sandwich_orders:
    sandwich_orders.remove('пастрами')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("Я сделал тебе " + sandwich.title() + " сэндвич!")
    finished_sandwiches.append(sandwich)

print("\nПриготовленные сэндвичи: ")

for finished_sandwich in finished_sandwiches:
    print("\t", finished_sandwich.title())
