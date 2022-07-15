n = int(input())
print(*range(15, n, 15)) if n < 100 else print('слишком большое значение n')