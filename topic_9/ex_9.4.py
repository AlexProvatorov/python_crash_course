"""
Посетители: начните с программы из упражнения 9.1. Добавьте атрибут 
number_served со значением по умолчанию 0; он представляет количество 
обслуженных посетителей. Создайте экземпляр с именем restaurant. Выведите 
значение number_served, потом измените и выведите снова. Добавьте метод с именем
set_number_served(), позволяющий задать количество обслуженных посетителей. 
Вызовите метод с новым числом, снова выведите значение. Добавьте метод с именем 
increment_number_served(), который увеличивает количество обслуженных 
посетителей на заданную величину. Вызовите этот метод с любым числом, которое 
могло бы представлять количество обслуженных клиентов — скажем, за один день. 
"""

class Restaurant():
    """Простая модель ресторана."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print("Название ресторана: " + self.restaurant_name.title() + ".")
        print("Тут вас ждет изумительная " + self.cuisine_type + " кухня!")
    
    def open_restaurant(self):
        print("Ресторан " + self.restaurant_name.title() + " открыт!")

    def read_number_served(self):
        """Выводим кол-во обслуженных посетителей."""
        print("Количество обслуженных посетителей: " + 
               str(self.number_served) + ".")

    def set_number_served(self, num):
        """Метод позволяет задать кол-во посетителей."""
        if num >= self.number_served:
            self.number_served = num
        else:
            print("Вы не можете задать меньшее число пометителей!")
    
    def increment_number_served(self, new_num):
        """Метод изменяет кол-во посетителей с приращением."""
        if new_num <= 0:
            print("Вы не можете уменьшать число посетителей!")
            self.number_served += new_num
        else:
            self.number_served += new_num

restautant_1 = Restaurant('миямото', 'японская')
restautant_1.describe_restaurant()
restautant_1.open_restaurant()
restautant_1.number_served = 3
restautant_1.read_number_served()
restautant_1.number_served = 8
restautant_1.read_number_served()

restautant_2 = Restaurant('сашими', 'японская')
restautant_2.describe_restaurant()
restautant_2.open_restaurant()
restautant_2.set_number_served(12)
restautant_2.read_number_served()
restautant_2.increment_number_served(3)
restautant_2.read_number_served()
restautant_2.set_number_served(9)
restautant_2.read_number_served()
restautant_2.increment_number_served(1)
restautant_2.read_number_served()