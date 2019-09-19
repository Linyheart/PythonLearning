# 4.演示==与is的区别
print("'=='表示比较前后对象的值是否相等，我们运行代码：a = [1, 2, 3] 和 b = [1, 2, 3]")
a = [1, 2, 3]
b = [1, 2, 3]
print("此时\" a == b \"返回值为：")
print(a == b)
print("而'is'表示比较前后对象的id（身份标识）是否相等。")
print("\" c is d \"返回值为：")
print(a is b)
print("我们可以看到a和b的id是不相同的：")
print(id(a))
print(id(b))