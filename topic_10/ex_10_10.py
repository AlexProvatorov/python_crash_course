"""

Частые слова: зайдите на сайт проекта «Гутенберг» (http://gutenberg.org/) и
найдите несколько книг для анализа. Загрузите текстовые файлы этих произведений
или скопируйте текст из браузера в текстовый файл на вашем компьютере. Для
подсчета количества вхождений слова или выражения в строку можно воспользовать-
ся методом count(). Например, следующий код подсчитывает количество вхождений
‘row’
в строке:
>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3
Обратите внимание: преобразование строки к нижнему регистру функцией lower()
позволяет найти все вхождения искомого слова независимо от регистра.
Напишите программу, которая читает файлы из проекта «Гутенберг» и определяет
количество вхождений слова ‘the’ в каждом тексте.

"""
def counts_the(file_name):
    """Функция считает кол-во слов 'the' в предложенном тексте."""
    try:
        with open(file_name, 'r') as file_object:
            contents = file_object.read()
            contents = contents.lower()
            words = contents.count('the')
            print("В файле", file_name, "обнаружено", words, "слов 'the'.")
    except FileNotFoundError:
        print("Файл", file_name, "не найден!")

files = ["topic_10/rebel_women.txt", "topic_10/black_mirror.txt",
         "topic_10/reading_the_weather.txt"]
for file in files:
    counts_the(file)