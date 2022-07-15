from car import Car

my_new_car = Car('mersedes', 'a class', 2020)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(28)
my_new_car.read_odometer()
