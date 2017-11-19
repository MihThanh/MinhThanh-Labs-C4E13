from urllib.request import urlopen
from bs4 import BeautifulSoup
#down web
html = urlopen("http://dantri.com.vn")
html_content = html.read().decode('utf8')
html.close()

#create BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
ul_news = soup.find('ul', 'ul1 ulnew')
# print(ul_news.prettify())
# tạo list các thẻ li
li_new_list = ul_news.find_all('li')
for li in li_new_list:
    # print(li.prettify())
    a_detail = li.h4.a
    # lấy ra attribute
    title = a_detail['title']
    # print(a_detail.prettify)
    # print(title)
    # content = a_detail.string
    print(title)
    print('-' * 20)
