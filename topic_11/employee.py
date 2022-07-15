class Employee():
    """Простая модель работника."""

    def __init__(self, first_name, last_name, annual_salary):
        """Инициализирует атрибуты имя фамилия и годовая ЗП."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, num=5000):
        """Проверка на величину прибавки к ЗП."""
        self.annual_salary += num