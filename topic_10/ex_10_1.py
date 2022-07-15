"""

Изучение Python: откройте пустой файл в текстовом редакторе и напишите несколько
строк текста о возможностях Python. Каждая строка должна начинаться с фразы:
«In Python you can...» Сохраните файл под именем learning_python.txt в каталоге,
использованном для примеров этой главы. Напишите программу, которая читает файл
и выводит текст три раза: с чтением всего файла, с перебором строк объекта файла
и с сохранением строк в списке с последующим выводом списка вне блока with.

"""
file_path = 'topic_10/learn_python.txt'

#Чтение всего файла и его вывод
with open(file_path) as file_object:
    contents = file_object.read()
    print("\n" + contents)

print('-' * 60)

#Чтение с перебором строк файла и их вывод.
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

print('-' * 60)

#Перебор строк объкта файла и сохранение их в списке, вывод вне 'with'.
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())