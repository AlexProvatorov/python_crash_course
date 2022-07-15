def build_person(first, last, age = ''):
    """Возвращает словарь с информацией о человеке"""

    if age:
        person = {'first_n': first, 'last_n': last, 'age': age,}
    else:
        person = {'first_n': first, 'last_n': last,}   
    return person

programmer = build_person('alex', 'satan')
print(programmer, "\n")

programmer = build_person('alex', 'satan', age = 21)
print(programmer, "\n")
