# 12.用str.format()输出一个三行 (含表头)三列表格
print('{:^{}}'.format("姓名", 10), end="\t\t")
print('{:^{}}'.format("学科", 10), end="\t\t")
print('{:^{}}'.format("成绩", 10))
print('{:<{}}'.format("张三", 10), end="\t\t")
print('{:<{}}'.format("数学", 10), end="\t\t")
print('{:>{}}'.format(90.5, 10))
print('{:<{}}'.format("李四", 10), end="\t\t")
print('{:<{}}'.format("语文（阅读）", 10), end="\t")
print('{:>{}}'.format(8.0, 10))
# :^ ：居中；:< ：左对齐；:> ：右对齐
# \t 制表符

