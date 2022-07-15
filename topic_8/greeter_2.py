def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

my_list = ['alex', 'criss', 'daniel']
greet_users(my_list)