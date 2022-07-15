"""

Ошибки без уведомления: измените блок except из упражнения 10-8 так, чтобы при
отсутствии файла программа продолжала работу, не уведомляя пользователя о
проблеме.

"""
def file_reader(file_name):
    """Простая читалка файлов."""
    try:
        with open(file_name, 'r') as file_object:
            contents = file_object.read()
            print(contents)
    except FileNotFoundError:
        pass

files = ["topic_10/cats.txt", "topic_10/parrots.txt", "topic_10/dogs.txt"]
for file in files:
    file_reader(file)