"""
Допустим, компания печатает на 3D-принтере модели, предоставленные пользователем.
Проекты хранятся в списке, а после печати перемещаются в отдельный список.
В следующем примере приведена реализация, не использующая функции:
"""
#Создаем пустой и полный список
unprinted_disign = ['car', 'robot', 'cap']
complited_models = []

#Перебераем полный список попутно перенося значения в пустой список
while unprinted_disign:
    current_model = unprinted_disign.pop()
    print("Напечатанная модель: " + current_model + ".")
    complited_models.append(current_model)

#Выводим все готовые модели
print("\nЗавершенные проэкты:")
for complited_model in complited_models:
    print(complited_model)
