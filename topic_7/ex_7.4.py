"""
Дополнения для пиццы: напишите цикл, который предлагает пользователю 
вводить дополнения для пиццы до тех пор, пока не будет введено значение
'quit’. При вводе каждого дополнения выведите сообщение о том, что это 
дополнение включено в заказ.
"""

message = "\nКакие дополнения для пиццы вы хотите?\n"
message += "Введите название дополнения(для выхода печатаем quit): "

while True:
    order = input(message)
    order = order.lower().strip()
    if order == 'quit':
        break
    else:
        print("Дополнение " + order + " включено в заказ!\n")