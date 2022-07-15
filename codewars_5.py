def square_digits(numbers):
    # Возводит в квадрат каждую цифру в значении.
    num_list = []
    square_list = []
    for number in str(numbers):
        num_list.append(number)
    for num in num_list:
        a = int(num) ** 2
        a = str(a)
        square_list.append(a)
    answer = "".join(square_list)
    return int(answer)


square_digits(9119)