import unittest
from city_functions import get_formatted_city_country

class CityTestCase(unittest.TestCase):
    """Тесты для 'city_functions.py'."""
    def test_city_country(self):
        """Имена вида ‘Santiago, Chile.’ работают правильно?"""
        city_country = get_formatted_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile.')
    

    def test_city_country_population(self):
        """Вывод 'Santiago, Chile population - 5000000.' работают правильно?"""
        city_country_population = get_formatted_city_country('santiago', 'chile', '5000000')
        self.assertEqual(city_country_population, 'Santiago, Chile population - 5000000.')

unittest.main()
