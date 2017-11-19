numbers = [1, 4 ,6, 18, 20, 16, 3, 2, 1]
n = int(input("Nhap so: "))
# if n in numbers:
#     for index, item in enumerate(numbers):
#         if(n == item):
#             print("{0} at {1}".format(item, index))
# else:
#     print("Not found")

#C2
found_index = -1
for index, item in enumerate(numbers):
    if n == numbers:
        found_index = index
        break
if found_index == -1:
    print("Not found")
else:
    print("Found: ", found_index)
