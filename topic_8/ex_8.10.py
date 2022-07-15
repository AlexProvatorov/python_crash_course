"""
Великие фокусники: начните с копии вашей программы из упражнения 8-9. 
Напишите функцию make_great(), которая изменяет список фокусников, 
добавляя к имени каждого фокусника приставку «Great». Вызовите функцию 
show_magicians() и убедитесь в том, что список был успешно изменен.
"""

def show_magicians(names):
    for name in names:
        print(name.title())

def make_great(names):
    for name in range(len(names)):
        names[name] = "great " + names[name]

magicians = ['devid blaine', 'garry gudini', 'steven frayne']

show_magicians(magicians)

make_great(magicians)
show_magicians(magicians)