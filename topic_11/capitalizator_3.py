import string

def to_jaden_case(text):
    #Capitalizator v0.3
    return string.capwords(text)

quote = "How can mirrors be real if our eyes aren't real"
answer = to_jaden_case(quote)

print(answer)