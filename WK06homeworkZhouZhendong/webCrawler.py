import requests
from bs4 import BeautifulSoup

urlHtml = "http://xteaching.com/book2019/list.php"
urlJson = "http://xteaching.com/book2019/listjson.php"
urlAddBook = "http://xteaching.com/book2019/add.php"


def get_from_html(url):
    page_html = requests.get(url)
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
    print(log_lines)
    log = open('bookInfoFromHtml.txt', 'w')
    log.writelines(log_lines)


