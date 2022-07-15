"""

Кошки и собаки: создайте два файла с именами cats.txt и dogs.txt. Сохраните
минимум три клички кошек в первом файле и три клички собак во втором. Напишите
программу, которая пытается прочитать эти файлы и выводит их содержимое на
экран. Заключите свой код в блок try-except для перехвата исключения
FileNotFoundError и вывода понятного сообщения об отсутствии файла. Переместите
один из файлов в другое место файловой системы; убедитесь в том, что код блока
except выполняется, как и положено.

"""
def file_reader(file_name):
    """Простая читалка файлов."""
    try:
        with open(file_name, 'r') as file_object:
            contents = file_object.read()
            print(contents)
    except FileNotFoundError:
        print("Файл " + file_name + " не найден!")

files = ["topic_10/cats.txt", "topic_10/parrots.txt", "topic_10/dogs.txt"]
for file in files:
    file_reader(file)