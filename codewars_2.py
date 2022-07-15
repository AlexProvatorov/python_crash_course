def high_and_low(numbers):
    # Возвращает большее и меньшее число в массиве
    numbers = numbers.split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    numbers = sorted(numbers)
    answer = str(numbers[-1]), str(numbers[0])
    return " ".join(answer) 