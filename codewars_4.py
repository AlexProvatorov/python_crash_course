def longest(s1, s2):
    # Сreates a formatted ordered string. 
    new_str = s1 + s2
    answer = set(new_str)
    return "".join(sorted(answer))

a1 = "xyaabbbccccdefww"
a2 = "xxxxyyyyabklmopq"

print(longest(a1, a2))