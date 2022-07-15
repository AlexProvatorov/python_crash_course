def disemvowel(user_string):
    # Removes all vowels in the string except 'y'. Returns the modified string.
    return "".join(s for s in user_string if s.lower() not in 'aeiou')

troll_string = "This website is for losers LOL!"
print(disemvowel(troll_string))