"""

Импортирование класса Restaurant: возьмите последнюю версию класса Restaurant и 
сохраните ее в модуле. Создайте отдельный файл, импортирующий класс Restaurant. 
Создайте экземпляр Restaurant и вызовите один из методов Restaurant, чтобы 
показать, что команда import работает правильно.

"""
from restaurant import Restaurant

sushi_house = Restaurant("суши хаус", "японская")
sushi_house.describe_restaurant()
sushi_house.open_restaurant()