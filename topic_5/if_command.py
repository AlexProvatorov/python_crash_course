#Простой пример
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Пример еще проще(eсли False, код игнорируется)
age = 18
print("\nЧисло больше или равно 18?")
if age >= 18:
    print("Да")

#if-else условия
age = 23
print("\nЧисло больше или равно 24?")
if age >= 24:
    print("Да")
else:
    print("Нет")
#if-elif-else
age = int(input("Введите свой возраст: "))
if age <= 6:
    cost = 0
elif age <= 18:
    cost = 50
else:
    cost = 100
print("Cтоимость билета составляет "+str(cost)+" рублей.")
