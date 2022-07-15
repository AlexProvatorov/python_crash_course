def solution(strng,markers):
    #strip comments func
    strng_list = strng.split('\n')
    for marker in markers:
        strng_list = [item.split(marker)[0].strip() for item in strng_list]
    return '\n'.join(strng_list).strip()

print(solution('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']), 'apples, pears\ngrapes\nbananas')
print('-' * 30)
print(solution('a #b\nc\nd $e f g', ['#', '$']), ' a\nc\nd')
print('-' * 30)
print(solution(' a #b\nc\nd $e f g', ['#', '$']), ' a\nc\nd')