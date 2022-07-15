#Срезы
motorcycles = ["bajaj", "ktm", "suzuki", "bmw", "harley devidson", "kawasaki", "honda", "ducati", "yamaha"]
#Выводит сообщение «The first three items in the list are:», а затем использует срез для
#вывода первых трех элементов из списка.
print("The first three items in the list are:")
for moto in motorcycles[:3]:
    print(moto.title())
#Выводит сообщение «Three items from the middle of the list are:», а затем использует
#срез для вывода первых трех элементов из середины списка.
print("\nThree items from the middle of the list are: ")
for moto in motorcycles[4:7]:
    print(moto.title())
##Выводит сообщение «The last three items in the list are:», а затем использует срез для
##вывода последних трех элементов из списка.
print("\nThe last three items in the list are: ")
for moto in motorcycles[-3:]:
    print(moto.title())