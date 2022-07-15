import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Тесты для класса Employee."""

    def setUp(self):
        """Экземпляр работника."""
        self.my_employee = Employee('Alex', 'Satan', 2500)

    def test_give_default_raise(self):
        """Проверка на дефолтное повышение в 5000."""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 7500)
    
    def test_give_custom_raise(self):
        """Проверка на кастомное повышение ЗП."""
        self.my_employee.give_raise(3000)
        self.assertEqual(self.my_employee.annual_salary, 5500)

unittest.main()