#Выполняю таск 3.10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(numbers)
numbers.append(10)
print(numbers)
numbers.insert(0, 11)
print(numbers)
del numbers[-1]
print(numbers)
dell_num = numbers.pop()
print(dell_num)
print(numbers)
numbers.remove(3)
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)
print(len(numbers))