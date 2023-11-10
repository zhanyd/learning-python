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
print('The first three item in the list are :', list5[0:3])
print(len(list5)//2-1)
print(len(list5)//2+1)
print('Three item from the middle of the list are :', list5[(len(list5)//2):(len(list5)//2+3)])
print('The last three item from the list are :', list5[len(list5) - 3 : ])
print('---------------')

my_t = (3,)
print(my_t[0])
