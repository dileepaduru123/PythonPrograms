li = [1, 2, 3, 4, 5]
lis = [2, 4, 5, 7]

li = set(li)
lis = set(lis)
print(li)
print(lis)

l3 = lis.difference(li)
print(l3)

li1 = [1, 2, 3, 4, 5]
lis2 = [2, 3, 4, 5, 6]

li1 = set(li1)
lis2 = set(lis2)
print(li1)
print(lis2)
l4 = lis2.difference(li1)
print(l4)


res = []
for i in lis:
    if i in li:
        li.remove(i)
    else:
        res.append(i)
    print(res)


for i in lis2:
    if i in li1:
        li1.remove(i)
    else:
        res.append(i)
print(res)
