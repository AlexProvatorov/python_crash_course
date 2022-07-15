def make_negative(number):
    # Меняем знак числа на противоположный.
    if number < 0:
        answer = number
    else:
        answer = -1 * number
    return answer

def make_negative(number):
    return -abs(number)