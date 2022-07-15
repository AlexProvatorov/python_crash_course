"""
Три ресторана: начните с класса из упражнения 9-1. Создайте три разных 
экземпляра, вызовите для каждого экземпляра метод describe_restaurant().
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

restaurant_1 = Restaurant('миямото', 'японская')
restaurant_2 = Restaurant('у белочки', 'лесная')
restaurant_3 = Restaurant('италити', 'итальянская')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()