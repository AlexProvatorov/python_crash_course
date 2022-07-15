def count_words(file_path):
    """Прога подсчитывает кол-во слов в текстовом файле"""
    try:
        with open(file_path, 'r') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("Файл " + file_path + " не найден!")
    else:
        words = contents.split()
        words_num = len(words)
        print("Файл " + file_path + " содержит " + str(words_num) + " слов.")

files = ['topic_10/rebel_women.txt', 'topic_10/moby_dick.txt', 
         'topic_10/reading_the_weather.txt']
for file_path in files:
    count_words(file_path)