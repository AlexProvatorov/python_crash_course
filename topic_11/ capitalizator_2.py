def to_jaden_case(text):
    #Capitalizator v 0.2
    old_text = text.split()
    new_text = []
    for word in old_text:
        new_word = word.capitalize()
        new_text.append(new_word)      
    answer = " ".join(new_text)
    return answer

quote = "How can mirrors be real if our eyes aren't real"
to_jaden_case(quote)