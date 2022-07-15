"""
Пользователи: создайте класс с именем User. Создайте два атрибута first_name и 
last_name, а затем еще несколько атрибутов, которые обычно хранятся в профиле 
пользователя. Напишите метод describe_user(), который выводит сводку с 
информацией о пользователе. Создайте еще один метод greet_user() для вывода 
персонального приветствия для пользователя. Создайте несколько экземпляров, 
представляющих разных пользователей. Вызовите оба метода для каждого 
пользователя. 
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

user_1 = User('alex', 'satan', 22, 'rostov', 'karate')
user_2 = User('criss', 'squirrel', 23, 'rostov', 'handcraft')

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()