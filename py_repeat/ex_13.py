# put your python code here
lst = ['москва', 'астрахань', 'новгород', 'димитровград', 'душанбе']
mark = ['ь', 'ъ', 'ы']
out = "НЕТ"
for i in range(len(lst)-1):
    if lst[i][-1] in mark:
        if lst[i+1][0] != lst[i][-2]:
            out = "ДА"
            break
    else:
        if lst[i+1][0] != lst[i][-1]:
            out = "ДА"
            break
print(out)