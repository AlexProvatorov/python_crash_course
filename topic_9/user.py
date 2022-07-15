"""Моделируем юзеров."""
class User():
    """Моделируем абстрактного юзера."""

    def __init__(self, first_name, last_name, age, location, hobby):
        self.first = first_name
        self.last = last_name
        self.full = first_name + " " + last_name
        self.age = age
        self.location = location
        self.hobby = hobby
    
    def describe_user(self):
        print("\nИнформация о пользователе:")
        print("Имя: " + self.first.title())
        print("Фамилия: " + self.last.title())
        print("Возраст: " + str(self.age))
        print("Местоположение: " + self.location.title())
        print("Хобби: " + self.hobby)
    
    def greet_user(self):
        print("Привет, " + self.full.title() + "!")