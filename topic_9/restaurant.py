"""Классы иммитируют заведения общепита."""
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
