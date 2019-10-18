import re


def check_phone_number(str_phone_number):
    regex = re.compile(r'(^\d{3}-)?\d{8}$')
    print(str_phone_number + " 是有效的电话号码格式吗？", end='')
    if regex.match(str_phone_number):
        print(True)
    else:
        print(False)


def check_zip_code(str_zip_code):
    regex = re.compile(r'^\d{6}$')
    print(str_zip_code + " 是有效的邮政编码格式吗？", end='')
    if regex.match(str_zip_code):
        print(True)
    else:
        print(False)


def check_url(str_url):
    regex = re.compile(r'^https?://\w+(?:\.[^\.]+)+(?:/.+)*$')
    print(str_url + " 是有效的网站网址格式吗？", end='')
    if regex.match(str_url):
        print(True)
    else:
        print(False)


def main():
    check_phone_number(input("请输入中国电话号码："))
    check_zip_code(input("请输入中国邮政编码："))
    check_url(input("请输入网站网址："))
