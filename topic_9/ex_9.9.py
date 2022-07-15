"""
Обновление аккумулятора: используйте окончательную версию программы 
electric_car.py из этого раздела. Добавьте в класс Battery метод с именем 
upgrade_battery(). Этот метод должен проверять размер аккумулятора и 
устанавливать мощность равной 85, если она имеет другое значение. Создайте 
экземпляр электромобиля с аккумулятором по умолчанию, вызовите get_range(), а 
затем вызовите get_range() во второй раз после вызова upgrade_battery(). 
Убедитесь в том, что запас хода увеличился.
"""


class Car():
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        """Инициализируем атрибуты описания авто."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print("This car has " + str(self.odometer_reading) + " miles.")

    def update_odometer(self, mileage):
        """Изменяем пробег вызовом функции + невозможность скрутить пробег."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Увеличивает показания одометра приращением + нельзя скрутить."""
        if miles <= 0:
            print("Enter the correct value!")
        else:
            self.odometer_reading += miles        
    
    def fill_gas_tank(self):
        """Заправь бензобак!"""
        print("Fill up the gas tank please!")


class Battery():
    """Простая модель аккума."""
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        """Описание объема аккума."""
        print("This car has a " + str(self.battery_size) + "kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 70:
            range = 240
        if self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."        
        print(message)
    
    def upgrade_battery(self):
        """Модернизация батареи авто."""

        if self.battery_size < 85:
            self.battery_size = 85
        else:
            print("The maximum battery capacity is already set!")

class ElectricCar(Car):
    """Простая модель электромобиля."""

    def __init__(self, make, model, year):
        """Инициализируем атрибуты класса родителя."""
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def fill_gas_tank(self):
        """У электромобилей нет бензобака."""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 's', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
