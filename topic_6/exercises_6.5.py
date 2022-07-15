rivers = {
    'нил': 'египет',
    'амазонка': 'америка',
    'конго': 'демократическая республика конго',
    }
for key, value in rivers.items():
    print(key.title() + " протекает через " + value.title() + ".")
print("\nРеки")
for river in rivers.keys():
    print(river.title() + ".")
print("\nСтраны")
for country in rivers.values():
    print(country.title() + ".")