"""
Суммирование миллиона чисел: создайте список чисел от 1 до 1 000 000, затем воспользуйтесь 
функциями min() и max() и убедитесь в том, что список действительно начинается с 1 и 
заканчивается 1 000 000. Вызовите функцию sum() и посмотрите, насколько быстро Python 
сможет просуммировать миллион чисел.
"""

numbers = list(range(1,1000001 ))
print(min(numbers))
print(max(numbers))
print(sum(numbers))