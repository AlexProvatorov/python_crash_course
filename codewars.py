def alphabet_position(text):
    # Finds the ordinal number of characters in the alphabet.
    answer = []
    for letter in text:
        if letter.isalpha():
            answer.append(ord(letter.lower()) - 96)
    answer = [str(num) for num in answer]
    return " ".join(answer)

text = "PythonMan"
print(alphabet_position(text))
