# 9.演示list的索引与切片
print("Python中列表的索引也是从0开始，我们也可以使用索引来截取（切片）列表中的元素。我们建立一个列表:")
print("listA = [123, 'xyz', 'Python', 'Java', 'C', 'C++', 'R', 'Javascript', 'C#', 'Matlab', 'Swift', 'Go']")
listA = [123, 'xyz', 'Python', 'Java', 'C', 'C++', 'R', 'Javascript', 'C#', 'Matlab', 'Swift', 'Go']
print("listA[0] = "+str(listA[0])+"    # 第一个元素")
print("listA[4] = "+str(listA[4])+"    # 第五个元素")
print("listA[-6] = "+str(listA[-6])+"    # 倒数第六个元素")
print("listA[5:] = "+str(listA[5:])+"    # 从第六个元素之后的所有元素，冒号后面默认为最大索引")
print("listA[:3] = "+str(listA[:3])+"    # 前三个元素，冒号前面默认为0")
print("listA[2:6] = "+str(listA[2:6])+"    # 第三到第六个元素")
print("listA[-3:] = "+str(listA[-3:])+"    # 后三个元素，索引为负时，冒号后面默认为0")
print("listA[:-4] = "+str(listA[:-4])+"    # 从第一个到倒数第五个元素，索引为负时，冒号前面默认为最小索引（或负无穷大）")
print("listA[-4:-2] = "+str(listA[-4:-2])+"    # 倒数第四个到倒数第三个元素")
print("listA[1:10:2] = "+str(listA[1:10:2])+"    # 从第二个元素开始，到第十个元素，以步长2索引")
print("我们还可以使用 index() 方法来在列表中查找索引。\n语法为：str.index(str, beg=0, end=len(string))")
print("str -- 指定检索的字符串\nbeg -- 开始索引，默认为0。\nend -- 结束索引，默认为字符串的长度。")
print("listA.index('Python') = "+str(listA.index('Python'))+"    # 'Python'的索引为2")
print("listA.index('Python', 5, 10)     # 会报错：'Python' is not in list")




