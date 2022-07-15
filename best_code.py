def longest(s1, s2):
    # Сreates a formatted ordered string.
    return "".join(sorted(set(s1+s2)))

a1 = "xyaabbbccccdefww"
a2 = "xxxxyyyyabklmopq"

print(longest(a1, a2))