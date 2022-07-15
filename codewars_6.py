def likes(names):
    # The function displays the number of likes.
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return names[0] + " likes this"
    elif len(names) == 2:
        return names[0] + " and " + names[1] + " like this"
    elif len(names) == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    else:
        others_num = str(len(names) - 2) + " others like this"
        return names[0] + ", " + names[1] + " and " + others_num

names = ['Alex', 'Bob', 'Max', 'Rob', 'John', 'Criss']
print(likes(names))