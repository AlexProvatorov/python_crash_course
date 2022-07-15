"""
Домашние животные: создайте несколько словарей, имена которых 
представляют клички домашних животных. В каждом словаре сохраните 
информацию о виде животного и имени владельца. Сохраните словари в 
списке с именем pets. Переберите элементы списка. В процессе перебора 
выведите всю имеющуюся информацию о каждом животном.
"""

rex = {
    'pet_name': 'rex',
    'owner_name': 'stan',
    'animal_type': 'dog',
    }

kiwi = {
    'pet_name': 'kiwi',
    'owner_name': 'max',
    'animal_type': 'parrot'
    }

rock = {
    'pet_name': 'rock',
    'owner_name': 'patrick',
    'animal_type': 'stone'
    }

pets = [rex, kiwi, rock,]

for pet in pets:
    print("Это " + pet['animal_type'] + " по имени " + pet['pet_name'].title() +
        ".")
    print("Его владельца зовут " + pet['owner_name'].title() + ".\n")