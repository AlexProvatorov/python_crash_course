#Знакомство с id(object)
number_1 = 5
number_2 = 12
print(number_1, number_2)
print(id(number_1), id(number_2))

number_1, number_2 = number_2, number_1
print(number_1, number_2)
print(id(number_1), id(number_2))

#Знакомство с type(object)
a = 1
b = 1.5
c = "ok"
d = [a, b, c]

print(type(a), type(b), type(c), type(d), sep='\n')