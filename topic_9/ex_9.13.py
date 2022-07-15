"""

Переработка с OrderedDict Rewrite: начните с упражнения 6.4, в котором
стандартный словарь используется для представления глоссария. Перепишите
программу с использованием класса OrderedDict и убедитесь в том, что 
порядок вывода совпадает с порядком добавления пар «ключ—значение» в 
словарь.

"""
from collections import OrderedDict

glossary = OrderedDict()

glossary['variable'] = 'хранит в себе значение.'
glossary['list'] = 'набор элементов следующих в определенном порядке.'
glossary['cycle'] = 'способ автоматизации повторяющихся задач.'
glossary['tuples'] = 'списки которые невозможно изменять.'
glossary['dictionary'] = 'структура данных объединяющая взаимосвязанную'
glossary['dictionary'] += ' информацию.'
glossary['concatenation'] = 'операция склеивания обычно строк.'
glossary['algorithm'] = 'это план, строгое исполнение которого приводит'
glossary['algorithm'] += ' к решению поставленной задачи.'
glossary['data'] = 'зарегистрированная информация приемлемая для '
glossary['data'] += 'общения, интерпретации, или обработки.'
glossary['function'] = 'кодовый модуль, имеющий своё имя, по которому '
glossary['function'] += 'он может быть вызван из других участков программы.'

for term, definition in glossary.items():
    print(term.title() + ": " + definition)