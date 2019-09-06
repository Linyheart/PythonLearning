import datetime

name = input('请输入您的姓名：')
birthYear = int(input('请输入您的出生年份：'))

age = datetime.date.today().year-birthYear
print("您好！ {0}。 您{1}岁。".format(name, age))
