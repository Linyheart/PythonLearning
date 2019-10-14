import requests
from bs4 import BeautifulSoup
import json


def main():
    url_html = "http://xteaching.com/book2019/list.php"
    url_json = "http://xteaching.com/book2019/listjson.php"
    url_add_book = "http://xteaching.com/book2019/add.php"

    add_book(url_add_book, "三体Ⅱ·黑暗森林", "刘慈欣", "2008")
    get_from_html(url_html)
    get_from_json(url_json)


def get_from_html(url):
    page_html = requests.get(url)
    page_html.encoding = 'utf-8'
    soup = BeautifulSoup(page_html.text, 'lxml')
    xml = soup.find_all('tr', class_="")
    book_info = []
    for i in range(1, len(xml)):
        book_info.append(xml[i].find_all('td', class_=""))

    book_info_unique = []
    for i in range(0, len(book_info)):
        if book_info[i] not in book_info_unique:
            book_info_unique.append(book_info[i])
    log_lines = []
    for i in range(0, len(book_info_unique)):
        for j in range(0, len(book_info_unique[i])):
            if j != len(book_info_unique[i]) - 1:
                log_lines.append(book_info_unique[i][j].string + ", ")
            else:
                log_lines.append(book_info_unique[i][j].string)
        log_lines.append("\n")
    log = open('bookInfoFromHtml.txt', 'w')
    log.writelines(log_lines)


def get_from_json(url):
    page_json = requests.get(url)
    page_json.encoding = 'utf-8'
    book_info = json.loads(page_json.text)

    book_info_unique = []
    for i in range(0, len(book_info)):
        if book_info[i] not in book_info_unique:
            book_info_unique.append(book_info[i])

    log_lines = []
    for i in range(0, len(book_info_unique)):
        for j in range(0, len(book_info_unique[i])):
            if j != len(book_info_unique[i]) - 1:
                log_lines.append(book_info_unique[i][j] + ",")
            else:
                log_lines.append(book_info_unique[i][j])
        log_lines.append("\n")

    log = open('bookInfoFromJson.txt', 'w')
    log.writelines(log_lines)


def add_book(url, name, author, year):
    response = requests.post(url, {"ti": name, "au": author, "y": year, "code": "2019pynet"})
    if response.status_code == 200:
        print(name + ", " + author + ", " + year + ", " + "添加成功！")
    else:
        print(name + ", " + author + ", " + year + ", " + "添加失败！请重试！")


main()