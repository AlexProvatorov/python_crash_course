def to_jaden_case(text):
    # capitalizator v 0.4
    new_text = []
    old_text = text.split()
    for word in old_text:
        new_text.append(word.capitalize())
    answer = " ".join(new_text)
    print(answer)

test = "How can mirrors be real if our eyes aren't real"
to_jaden_case(test)