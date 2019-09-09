import random
a = 17
# random.randint(0, 100)
b = 77
# random.randint(0, 100)
c = 88
# random.randint(0, 100)
list = [a, b, c]
print(list)
#方法一：
list1 = list
while True:
    if list1[0] < list1[1] & list1[1] < list1[2]:
        break
    random.shuffle(list1)
    print(list1)

#方法二：
list2 = list
if list2[0] > list2[1]:
    m = list2[0]
    list2[0] = list2[1]
    list2[1] = m
if list2[2] < list2[0]:
    m = list2[2]
    list2[2] = list2[1]
    list2[1] = list2[0]
    list2[0] = m
if list2[2] > list2[0] & list2[2] < list2[1]:
    m = list2[2]
    list2[2] = list2[1]
    list2[1] = m
print(list2)
