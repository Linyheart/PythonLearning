# 10.用户输入一个字符串，显示用户输入的字符串内容，并逐个显示字符的ASCII/UNICODE值
a = input("请输入一个字符串：")
print("您输入的字符串为："+str(a))
for letter in a:
    print(str(letter)+"\t的ASCII/UNICODE值为：\t"+str(ord(letter)))
