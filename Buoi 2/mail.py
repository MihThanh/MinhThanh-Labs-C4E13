from gmail import *
from random import choice
# Chọn random 1 file
file_names = ['mail1.html', 'mail2.html', 'mail3.html']
file_name = choice(file_names)
print(file_name)

reasons = ['Thành', 'Văn', 'Toán', '1', '2']
reason = choice(reasons)
# đọc file
fo = open(file_name,encoding="utf-8")
html1 = fo.read()
fo.close()
print(html1)
# 
html1 = html1.replace('{reason}',reason)
# gửi
gmail = GMail('c4e.lab@gmail.com','malong1996')
msg = Message('Test Message',to='c4e13.lab.huynq@gmail.com',html= html1)
gmail.send(msg)
