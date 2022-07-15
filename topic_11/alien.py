#Создание вложения словарей в один список
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

for alien_number in range(27):
    new_alien = {'color': 'blue', 'points': 20}
    aliens.append(new_alien)
for alien in aliens:
    print(alien)
print(str(len(aliens)))

for alien in aliens[0:3]:
    if alien ['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 25
for alien in aliens[0:5]:
    print(alien)