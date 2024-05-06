# первое задание
a = 1
b = 1
c = 1
print("a - ", id(a))
print("b - ", id(b))
print("c - ", id(c))


# второе задание
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("list1 - ", id(list1))
print("list2 - ", id(list2))


# третье задание
print(id(str(a)))
print(id(float(b)))
print(id(c))
print(id(str(list1)))
print(id(str(list2)))
