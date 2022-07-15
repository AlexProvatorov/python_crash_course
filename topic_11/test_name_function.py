import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'"""
    def test_first_last_name(self):
        """Имена вида 'Alex Satan' работают правильно?"""
        formatted_name = get_formatted_name('alex', 'satan')
        self.assertEqual(formatted_name, 'Alex Satan')

    def test_first_last_middle_name(self):
        """Имена вида 'Jessica Mary Alba' работают правильно?"""
        formatted_name = get_formatted_name('jessica', 'alba', 'mary')
        self.assertEqual(formatted_name, 'Jessica Mary Alba')

unittest.main()