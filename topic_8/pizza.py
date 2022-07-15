"""
Импортирование: возьмите за основу одну из написанных вами программ с одной
функцией. Сохраните эту функцию в отдельном файле. Импортируйте функцию в файл
основной программы и вызовите функцию каждым из следующих способов:
"""
#import имя_модуля
import pizza_making

pizza_making.make_pizza('огурчик', 'томатик', 'сырочек',)

#from имя_модуля import имя_функции
from pizza_making import make_pizza

make_pizza('рыба', 'сыр',)

#from имя_модуля import имя_функции as псевдоним
from pizza_making import make_pizza as mp

mp('пельмени', 'хинкали', 'сода',)

#import имя_модуля as псевдоним
import pizza_making as pm

pm.make_pizza('двойной сыр', 'колбаска', 'кукуруза',)

#from имя_модуля import *
from pizza_making import *

make_pizza('усталый карась', 'сыр с плесенью')