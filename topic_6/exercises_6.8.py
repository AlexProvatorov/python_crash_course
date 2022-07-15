#Создаем словари под именем животных, в словаре инфа о пэте, имя хозяина.
kesha = {'animal_type': 'попугай', 'owner': 'вовка',}
scooby = {'animal_type': 'собака', 'owner': 'шэги',}
boots = {'animal_type': 'обезьяна', 'owner': 'даша',}
#Создаем список словарей животных.
pets = [kesha, scooby, boots]
#Выводим инфу из словарей.
for pet in pets:
    print("Тип животного: " + pet['animal_type'].title())
    print("Владелец животного: " + pet['owner'].title() + "\n")