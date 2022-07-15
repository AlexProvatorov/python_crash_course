def square_digits(nums):
    # Возводит в квадрат каждую цифру в значении и объединяет их.
    nums_list = [num for num in str(nums)]
    square_list = [str(int(num) ** 2) for num in nums_list]
    answer = "".join(square_list)
    return int(answer)

square_digits(9119)