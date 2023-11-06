list1 = range(1, 1000001)
print(min(list1))
print(max(list1))
print(sum(list1))

print('---------------')

list2 = range(1, 20, 2)
for i in list2:
    print(i)

print('---------------')

list3 = []
for i in range(1, 10):
    item = i * 3
    list3.append(item)
    print(item)

print('---------------')

list4 = []
for i in range(1, 10):
    item = i ** 3
    list4.append(item)
print(list4)    

print('---------------')
list5 = [value ** 3 for value in range(1, 10)]
print(list5)
