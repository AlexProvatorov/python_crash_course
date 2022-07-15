numbers = list(map(int, input()))
answer = 1
i = 1
while i <= len(numbers):
    for number in numbers:
        answer *= number
        i += 1
print(answer)