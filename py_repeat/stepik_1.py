# put your python code here
m, n = map(int, input().split())
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
if m == 1 and n == 31:
    print("01.30 02.01")# последнее число 
elif m == 2 and n == 1:
    print("01.31 02.02")# первое число
elif m == 2 and n == 28:
    print("02.27 03.01")# последнее число
elif m == 3 and n == 1:
    print("02.28 03.02")# первое число
elif m == 3 and n == 31:
    print("03.30 04.01")# последнее число
elif m == 4 and n == 1:
    print("03.31 04.02")# первое число
elif m == 4 and n == 30:
    print("04.29 05.01")# последнее число
elif m == 5 and n == 1:
    print("04.30 05.02")# первое число
elif m == 5 and n == 31:
    print("05.30 06.01")# последнее число
elif m == 6 and n == 1:
    print("05.31 06.02")# первое число
elif m == 6 and n == 30:
    print("06.29 07.01")# последнее число
elif m == 7 and n == 1:
    print("06.30 07.02")# первое число
elif m == 7 and n == 31:
    print("07.30 08.01")# последнее число
elif m == 8 and n == 1:
    print("07.31 08.02")# первое число
elif m == 8 and n == 31:
    print("08.30 09.01")# последнее число
elif m == 9 and n == 1:
    print("08.31 09.02")# первое число
elif m == 9 and n == 30:
    print("09.29 10.01")# последнее число
elif m == 10 and n == 1:
    print("09.30 10.02")# первое число
elif m == 10 and n == 31:
    print("10.30 11.01")# последнее число
elif m == 11 and n == 1:
    print("10.31 11.02")# первое число
elif m == 11 and n == 30:
    print("11.29 12.01")# последнее число
elif m == 12 and n == 1:
    print("11.30 12.02")# первое число
elif m == 12 and n == 31:
    print("12.30 01.01")# последнее число
elif m == 1 and n == 1:
    print("12.31 01.02")# первое число
else:
    if m <= 9:
        m = f"0{m}"
    if n <= 8:
        print(f"{m}.0{n - 1} {m}.0{n + 1}")
    if n == 9 or n == 10:
        print(f"{m}.0{n - 1} {m}.{n + 1}")
    if n >= 11:    
        print(f"{m}.{n-1} {m}.{n+1}")