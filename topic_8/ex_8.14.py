"""
Автомобили: напишите функцию для сохранения информации об автомобиле в 
словаре. Функция всегда должна возвращать производителя и название 
модели, но при этом она может получать произвольное количество 
именованных аргументов. Вызовите функцию с передачей обязательной 
информации и еще двух пар «имя—значение» (например, цвет и 
комплектация). Ваша функция должна работать для вызовов следующего вида:
car = make_car(‘subaru’, ‘outback’, color=’blue’, tow_package=True)
Выведите возвращаемый словарь и убедитесь в том, что вся информация была
сохранена правильно.
"""

def make_car(brand, model, **car_info):
    car_profile = {}
    car_profile['brand'] = brand
    car_profile['model'] = model
    for key, value in car_info.items():
        car_profile[key] = value
    return car_profile

car_1 = make_car('tesla', 'model s', color='black', equipment='standard')
print(car_1)