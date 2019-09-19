# 8.演示break和continue的功能
print("Python中的break语句，可以打破最小封闭for或while循环。")
print("我们定义一个字符串 a = 'Python' ，并使用for循环遍历字符串。")
a = 'Python'
for letter in a:
    print(letter, end=" ")
print("\n我们可以使用break语句在输出h后终止循环，停止遍历：")
for letter in a:
    print(letter, end=" ")
    if letter == 'h':
        break
print("\nPython中的continue语句，可以跳过当次的for或while循环。我们可以使用continue语句跳过输出h：")
for letter in a:
    if letter == 'h':
        continue
    print(letter, end=" ")

