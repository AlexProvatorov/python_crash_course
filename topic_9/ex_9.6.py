"""
Киоск с мороженым: киоск с мороженым — особая разновидность ресторана. Напишите 
класс IceCreamStand, наследующий от класса Restaurant из упражнения 9.1 или 
упражнения 9.4. Подойдет любая версия класса; просто выберите ту, которая вам 
больше нравится. Добавьте атрибут с именем flavors для хранения списка сортов 
мороженого. Напишите метод, который выводит этот список. Создайте экземпляр 
IceCreamStand и вызовите этот метод.
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

class IceCreamStand(Restaurant):
    """Простая модель ларька с мороженым"""
    
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def describe_restaurant(self):
        print("Название ресторана: " + self.restaurant_name.title() + ".")
        print("Тут вас ждет изумительное " + self.cuisine_type + "!")

    def show_flavors(self):
        print("В наличии есть мороженное с такими ароматизаторами:")
        for flavor in self.flavors:
            print("\t- " + flavor)

restaurant_1 = IceCreamStand('happy squirrel', 'мороженное')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_1.flavors = ['ваниль', 'банан', 'клубника', 'шоколад']
restaurant_1.show_flavors()