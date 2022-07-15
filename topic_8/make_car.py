def make_car(brand, model, **car_info):
    """Функция создает словарь авто с названием бренда, модели и доп 
       инфой"""
    car_profile = {}
    car_profile['brand'] = brand
    car_profile['model'] = model
    for key, value in car_info.items():
        car_profile[key] = value
    return car_profile