#Проверка условий
num = '23'
num_1 = '13'

print("Номер = 23?")
print(num == '23')
print("Номер = 22?")
print(num == '22')

print("Номер не равен 26?")
print(num != '26')
print("Номер не равен 23?")
print(num != '23')

print("Номер меньше или равен 23?")
print(num <= '23')
print("Номер больше или равен 24?")
print(num >= '24')

print("Числа 23 и 13?")
print(num == '23' and num_1 == '13')
print("Числа 23 и 15?")
print(num == '23' and num_1 == '15')

print("Числа 23 или 13?")
print(num == '23' or num_1 == '13')
print("Числа 23 или 15?")
print(num == '8' or num_1 == '9')