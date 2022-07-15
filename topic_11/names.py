from name_function import get_formatted_name

while True:

    print("\nВведите данные для форматирования('q' для выхода в любой момент)")
    first = input("Введите ваше имя: ")
    if first.lower() == 'q':
        break
    last = input("Введите вашу фамилию: ")
    if last.lower() == 'q':
        break
    middle = input("Введите ваше второе имя: ")
    if middle.lower() == 'q':
        break
    elif middle.lower() == '':
        pass

    formatted_name = get_formatted_name(first, last, middle)
    print("\tВаше имя отформатированно: " + formatted_name + ".")