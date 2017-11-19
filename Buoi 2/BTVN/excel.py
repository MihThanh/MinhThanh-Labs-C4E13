import pyexcel

dic = [
    {
        "Name" : "Thanh",
        "Age" : 22
    },
    {
        "Name" : "Oanh Oanh",
        "Age" : 22
    },
    {
        'Name' : 'Tuan',
        'Age' : 25
    }
]
pyexcel.save_as(records = dic, dest_file_name = "convert1.xls")

# Lấy dữ liệu từ file
# records = p.iget_records(file_name = "convert.xls")
# for record in records:
#     print("{0} is aged at {1}".format(record['Name'],record['Age']))
# p.free_resources()
