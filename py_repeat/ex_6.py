# put your python code here
n = int(input()) # получаем кол-во лет
i = 0
answer = 1000
while i != n:
    answer += (answer * 5) / 100
    i += 1
print(round(answer, 2))