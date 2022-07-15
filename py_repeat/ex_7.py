# put your python code here
p = [0] * 10
while sum(p) < 5:
    i = int(input())
    p[i] = 1
print(*p)