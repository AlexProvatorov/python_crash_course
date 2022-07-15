# put your python code here
n, m = map(int, input().split())
while n <= m:
    n2 = n ** 2
    n += 1
    print(f"{n2}", end=' ')