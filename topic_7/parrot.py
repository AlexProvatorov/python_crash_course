#Попугай цикла while

prompt = "\nВведите любое слово или фразу и я повторю за вами!"
prompt += "\nЧтобы попугай замолчал, введите слово: 'замолчи'.\nВведите фразу: "

active = True
while active:
    message = input(prompt)

    if message == 'замолчи':
        active = False
    else:
        print(message) 
