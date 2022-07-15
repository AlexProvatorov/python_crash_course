"""
Ресторан: создайте класс с именем Restaurant. Метод __init__() класса Restaurant
должен содержать два атрибута: restaurant_name и cuisine_type. Создайте метод 
describe_restaurant(), который выводит два атрибута, и метод open_restaurant(), 
который выводит сообщение о том, что ресторан открыт. Создайте на основе своего 
класса экземпляр с именем restaurant. Выведите два атрибута по отдельности, 
затем вызовите оба метода.
"""

class Restaurant():
    """Простая модель ресторана"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("Название ресторана: " + self.restaurant_name.title() + ".")
        print("Тут вас ждет изумительная " + self.cuisine_type + " кухня!")
    
    def open_restaurant(self):
        print("Ресторан " + self.restaurant_name.title() + " открыт!")

restautant_1 = Restaurant('миямото', 'японская')
restautant_1.describe_restaurant()
restautant_1.open_restaurant()
