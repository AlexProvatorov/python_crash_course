def get_formatted_name(first_name, last_name):
    """Возвращает красиво отформатированное полное имя."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

#Бесконечный цикл
active = True

while active:
    print("\nПожалуйста ваши данные: ")
    print("(Для завершения работы программы введите 'q' в любое время.)")

    f_name = input("Введите имя: ")
    if f_name == 'q':
        break

    l_name = input("Введите фамилию: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)

    print("\nЗдравствуйте, " + formatted_name + "!")

    active = input("\nЖелаете завершить работу программы?\n(yes/no) ")
    if active == 'yes':
        active = False

