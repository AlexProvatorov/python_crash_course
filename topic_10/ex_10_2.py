"""

Изучение C: метод replace() может использоваться для замены любого слова в
строке другим словом. В следующем примере слово ‘dog’ заменяется словом ‘cat’:
message = "I really like dogs."
message.replace('dog', 'cat')
Вывод: I really like cats.
Прочитайте каждую строку из только что созданного файла learning_python.txt и
замените слово Python названием другого языка, например C. Выведите каждую
измененную строку на экран.

"""
file_path = 'topic_10/learn_python.txt'

#Через перебор списка строк.
with open(file_path) as file_object:
    for line in file_object:
        line = line.replace('Python', 'C')
        print(line.rstrip())

print('-' * 60)

#Через чтение файла целиком.
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.replace('Python', 'C'))