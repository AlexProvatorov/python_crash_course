def to_jaden_case(text):
    #Capitalizator v 0.1
    position = text.find("'")
    if position == -1:
        return text.title()
    else:
        answer = text[:position].title() + text[position:position+2].lower()
        answer += text[position+2:].title()
        return answer

quote = "How can mirrors be real if our eyes aren't real"
a = to_jaden_case(quote)

print(a)