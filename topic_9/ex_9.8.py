"""
Привилегии: напишите класс Privileges. Класс должен содержать всего один атрибут
privileges со списком строк из упражнения 9.7. Переместите метод 
show_privileges() в этот класс. Создайте экземпляр Privileges как атрибут класса
Admin. Создайте новый экземпляр Admin и используйте свой метод для вывода списка
привилегий.
"""

class User():
    """Моделируем абстрактного юзера"""

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

class Privileges():
    """Класс описывает привилегии админа"""

    def __init__(self):
        self.privileges = ["разрешено добавлять сообщения", 
                           "разрешено удалять пользователей", 
                           "разрешено банить пользователей"]
    
    def show_privileges(self):
        print("Привилегии админа:")
        for privilege in self.privileges:
            print("\t- " + privilege + ";")

class Admin(User):
    """Моделируем админа"""

    def __init__(self, first_name, last_name, age, location, hobby):
        super().__init__(first_name, last_name, age, location, hobby)
        self.privileges = Privileges()

admin = Admin('alex', 'satan', 22, 'rostov', 'karate')
admin.describe_user()
admin.privileges.show_privileges()