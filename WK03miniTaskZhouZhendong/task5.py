# 5.演示可变对象与不可变对象
print("在Python中有可变对象和不可变对象。\n其中可变对象有：\tlist\tdict\n不可变对象有:\tint\t\tstring\t\tfloat\ttuple")
print("可变对象在变化时会直接在原来指向的内存空间上发生变化。")
print("我们创建一个可变对象 list1 = [1, 2, 3] ，它的id为：")
list1 = [1, 2, 3]
print(id(list1))
print("我们对它进行修改，添加一个元素 '4' ，此时它变化为：")
list1.append(4)
print(list1)
print("但是它的id不会发生变化：")
print(id(list1))
print("不可变对象在变化时会改变并指向新的内存空间。")
print("我们创建一个不可变对象 a = 37 ，它的id为：")
a = 37
print(id(a))
print("我们对它进行修改，执行代码 'a = a + 1'  ，此时它变化为：")
a = a + 1
print(a)
print("它的id已经发生变化：")
print(id(a))
