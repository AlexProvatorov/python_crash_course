import make_car
#Импортирование всего модуля
car_1 = make_car.make_car('tesla', 'model x', color='blue', 
                          equipment='standard')
print(car_1)
#Импортирование конкретных функция
from make_car import make_car
car_1 = make_car('tesla', 'model s', color='black', equipment='standard')
print(car_1)
#Назначение псевдонима функции
from make_car import make_car as mc
car_1 = mc('tesla', 'model 3', color='red', equipment='standard')
print(car_1)
#Назначение псевдонима для модуля
import make_car as m
car_1 = m.make_car('tesla', 'model 3', color='yellow', equipment='standard')
print(car_1)
#Импортировать все функции в модуле
from make_car import *
car_1 = make_car('tesla', 'model x', color='blue', 
                          equipment='standard')
print(car_1)