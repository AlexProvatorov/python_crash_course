def disemvowel(user_string):
    # Removes all vowels in the string except 'y'. Returns the modified string.
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_string = ''
    for symbol in user_string:
        if symbol.lower() not in vowels:
            new_string += symbol
    return new_string

troll_string = "This website is for losers LOL!"
print(disemvowel(troll_string))