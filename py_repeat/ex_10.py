lst_in = ['Муму', 'Евгений Онегин', 'Сияние', 'Мастер и Маргарита', 'Пиковая дама', 'Колобок']
i = -1
while i < len(lst_in) - 1:
    i += 1
    if " " in lst_in[i]:
        continue
    else:
        print(lst_in[i], end = ' ')