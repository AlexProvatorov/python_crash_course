"""Позиционные аргументы"""

def describe_pet(animal_type, animal_name):
    print("Мое животное это " + animal_type + ".")
    print("Его зовут " + animal_name.title() + ".")

describe_pet(animal_type = 'кактус', animal_name = 'генри')