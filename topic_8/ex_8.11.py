"""
Фокусники без изменений: начните с программы из упражнения 8-10. 
Вызовите функцию make_great() и передайте ей копию списка имен 
фокусников. Поскольку исходный список остался неизменным, верните новый 
список и сохраните его в отдельном списке. Вызовите функцию 
show_magicians() с каждым списком, чтобы показать, что в одном списке 
остались исходные имена, а в другом к имени каждого фокусника добавилась
приставка «Great».
"""

def show_magicians(names):
    for name in names:
        print(name.title())

def make_great(names):
    for name in range(len(names)):
        names[name] = "great " + names[name]

magicians = ['devid blaine', 'garry gudini', 'steven frayne']

make_great(magicians[:])