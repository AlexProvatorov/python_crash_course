"""
Администратор: администратор — особая разновидность пользователя. Напишите класс
с именем Admin, наследующий от класса User из упражнения 9.3 или упражнения 9.5. 
Добавьте атрибут privileges для хранения списка строк вида «разрешено добавлять 
сообщения», «разрешено удалять пользователей», «разрешено банить пользователей» 
и т. д. Напишите метод show_privileges() для вывода набора привилегий 
администратора. Создайте экземпляр Admin и вызовите свой метод. 
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

class Admin(User):
    """Моделируем админа"""

    def __init__(self, first_name, last_name, age, location, hobby):
        super().__init__(first_name, last_name, age, location, hobby)
        self.privileges = ["разрешено добавлять сообщения", 
                           "разрешено удалять пользователей", 
                           "разрешено банить пользователей"]
    
    def show_privileges(self):
        print("Привилегии админа:")
        for privilege in self.privileges:
            print("\t- " + privilege + ";")

admin = Admin('alex', 'satan', 22, 'rostov', 'karate')
admin.describe_user()
admin.show_privileges()