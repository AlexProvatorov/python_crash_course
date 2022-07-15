"""
Кубы: результат возведения числа в третью степень называется кубом. Например,
куб 2 записывается в языке Python в виде 2**3. Создайте список первых 10 кубов (то есть
кубов всех целых чисел от 1 до 10) и выведите значения всех кубов в цикле for.
"""

"""
#Вариант 1
cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
    print(cube)
print(cubes)
"""

#Вариант 2
cubes = []
for value in range(1,11):
    cubes.append(value**3)
    print(value**3)
print(cubes)

