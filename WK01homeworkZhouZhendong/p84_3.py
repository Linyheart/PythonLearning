import random
a = random.randint(0, 100)
b = random.randint(0, 100)
c = random.randint(0, 100)
list0 = [a, b, c]

# 方法一：
list1 = [a, b, c]
while True:
    if list1[0] < list1[1] < list1[2]:
        break
    random.shuffle(list1)

# 方法二：
list2 = [a, b, c]
if list2[0] > list2[1]:
    m = list2[0]
    list2[0] = list2[1]
    list2[1] = m
if list2[2] < list2[0]:
    m = list2[2]
    list2[2] = list2[1]
    list2[1] = list2[0]
    list2[0] = m
if list2[0] < list2[2] < list2[1]:
    m = list2[2]
    list2[2] = list2[1]
    list2[1] = m

print("原始值：  a="+str(list0[0])+"  b="+str(list0[1])+"  c="+str(list0[2]))
print("（方法一）升序值：  a="+str(list1[0])+"  b="+str(list1[1])+"  c="+str(list1[2]))
print("（方法二）升序值：  a="+str(list2[0])+"  b="+str(list2[1])+"  c="+str(list2[2]))
