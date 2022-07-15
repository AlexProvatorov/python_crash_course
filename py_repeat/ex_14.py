# put your python code here
text = input().lower()
if "ра" not in text:
    print(-1)
else:
    for i in range(0, len(text) - 1):
        if "р" in text[i] and "а" in text[i+1]:
            print(i, end = ' ')