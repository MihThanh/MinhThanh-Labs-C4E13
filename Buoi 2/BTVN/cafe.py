# tìm thẻ table-> tbody
#
# all thẻ tr
#
# for tr rồi tìm ra all ds
#
# for as ->string

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
html = urlopen("http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn")
html_content = html.read().decode('utf8')
html.close

soup = BeautifulSoup(html_content, 'html.parser')
table_news = soup.find('table', id = 'tableContent')
tr_list_new = table_news.find_all('tr')

for tr in tr_list_new:
    td_list_new = tr.find_all('td')
    for td in td_list_new:
        td_content = td.string
        print(td_content)
        print('*' *20)
