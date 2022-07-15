# put your python code here
names = ['петр', 'анна', 'иван', 'сергей', 'михаил', 'федор']
i = 0
answer = "НЕТ"
while i < len(names):
    if names[i][0] != names[i][-1]:
        i += 1
        continue
    elif names[i][0] == names[i][-1]:
        answer = "ДА"
        break
print(answer)