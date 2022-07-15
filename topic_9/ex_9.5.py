"""
Попытки входа: добавьте атрибут login_attempts в класс User из упражнения 9.3. 
Напишите метод increment_login_attempts(), увеличивающий значение login_attempts
на 1. Напишите другой метод с именем reset_login_attempts(), обнуляющий значение
login_attempts. Создайте экземпляр класса User и вызовите 
increment_login_attempts() несколько раз. Выведите значение login_attempts, 
чтобы убедиться в том, что значение было изменено правильно, а затем вызовите 
reset_login_attempts(). Снова выведите login_attempts и убедитесь в том, что 
значение обнулилось.
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
        self.login_attempts = 0
    
    def describe_user(self):
        print("\nИнформация о пользователе:")
        print("Имя: " + self.first.title())
        print("Фамилия: " + self.last.title())
        print("Возраст: " + str(self.age))
        print("Местоположение: " + self.location.title())
        print("Хобби: " + self.hobby)
    
    def greet_user(self):
        print("Привет, " + self.full.title() + "!")

    def read_login_attempts(self):
        print("Попытки входа в систему: " + str(self.login_attempts) + ".")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user_1 = User('alex', 'satan', 22, 'rostov', 'karate')
user_2 = User('criss', 'squirrel', 23, 'rostov', 'handcraft')

user_1.describe_user()
user_1.read_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.read_login_attempts()
user_1.reset_login_attempts()
user_1.read_login_attempts()
