from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://nhaczingmp3.com/")
html_content = html.read().decode("utf8")
html.close()

soup = BeautifulSoup(html_content, "html.parser")
div_new_list = soup.find('div', 'widget-box')
ul_new_list = div_new_list.find('ul')
li_new_list = ul_new_list.find_all('li')
for li in li_new_list:
    a = li.div.h3.a
    title = a.string
    print(title)
    print('*' *20)
