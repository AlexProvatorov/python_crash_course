def order(sentence):
    words = sentence.split()
    order = sorted(words, key=)

def int_from_list(word):
    for letter in word:
        if letter in word.isdigit()

a = "4of Fo1r pe6ople g3ood th5e the2"
print(order(a))

def order(sentence):
    words = sentence.split()
    ordered_words = sorted(words, key=int_from_word)
    return " ".join(ordered_words)

def int_from_word(word):
    for character in word:
        if character.isdigit():
            return int(character)
    return None