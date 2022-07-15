#Создание среза списка(слайсов)
players = ['alex','jack','john','gordon','criss']
print(players[0:2])
print(players[1:])
print(players[:4])
print(players[-3:])

#перебор среза(выводим первые 3 имя)
for player in players[:3]:
    print(player.title())

#копирование списка
copy_players = players[:]
print(copy_players)
copy_players.append('max')
print(copy_players)
