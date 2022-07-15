#Билет в парк атракционов if-elif-else
age = int(input("Введите свой возраст: "))
if age <= 6:
    cost = 0
elif age <= 18:
    cost = 50
else:
    cost = 100
print("Стоимость билета составит " + str(cost) + " рублей!")