favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    } 

polls = ['phil','alex','sarah','jen','criss','edward',]

for name in polls:
    if name in favorite_languages.keys():
        print(name.title() + ", уже прошел опрос, спасибо!")
    else:
        print(name.title() + ", пожалуйста пройдите опрос.")