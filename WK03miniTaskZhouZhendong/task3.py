# 3.写函数，参数为int,在屏幕上输出其: 10 进制，2进制、8进制、16 进制形式
a = int(input("请输入想要转换的数字："))


def transform(num):
    print("10进制形式："+"\t"+str(int(num)))
    print("2进制形式："+"\t"+str(bin(num)))
    print("8进制形式："+"\t"+str(oct(num)))
    print("16进制形式："+"\t"+str(hex(num)))


transform(a)
