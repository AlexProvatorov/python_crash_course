"""Моделируем админа."""
from user import User

class Admin(User):
    """Моделируем админа."""

    def __init__(self, first_name, last_name, age, location, hobby):
        super().__init__(first_name, last_name, age, location, hobby)
        self.privileges = Privileges()


"""Описываем привилегии."""
class Privileges():
    """Класс описывает привилегии админа."""

    def __init__(self):
        self.privileges = ["разрешено добавлять сообщения", 
                           "разрешено удалять пользователей", 
                           "разрешено банить пользователей"]
    
    def show_privileges(self):
        print("Привилегии админа:")
        for privilege in self.privileges:
            print("\t- " + privilege + ";")
