"""Простая читалка файлов."""
file_path = '/home/alex_satan/my_code/topic_10/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

file_path = '/home/alex_satan/my_code/topic_10/pi_digits.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

file_path = '/home/alex_satan/my_code/topic_10/pi_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())