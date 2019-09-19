# 1.sys.argv的功能
import sys
print("sys.argv是从程序外部获取参数的桥梁，可以看做一个列表。\n\n其中sys.argv[0]值为代码文件本身的路径，后面的列表值为用户从外部输入的参数值。\n")
print("本文件的路径为：\n")
print("C:\\Users\\Administrator\\Desktop\\Python\\PythonLearning\\WK03miniTaskZhouZhendong\\task1.py\n")
print("输出sys.argv[0]结果为：\n")
print(sys.argv[0]+"\n")
print("我们在外部运行此代码时分别输入了参数：arg1和arg2\n")
print("则输出sys.argv[1]和sys.argv[2]的结果分别为：\n")
print(sys.argv[1]+"\n")
print(sys.argv[2]+"\n")
print("若我们在运行时不输入参数，则会报错“list index out of range”（索引超出列表范围），\n\n因为若没有输入参数，sys.argv列表就只有文件路径一个元素\n")

