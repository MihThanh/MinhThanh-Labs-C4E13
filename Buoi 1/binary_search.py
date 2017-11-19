numbers = [1, 3, 5, 7, 12, 64, 89, 100, 111, 122]
n = int(input("Nhap so: "))
left = 0
right = len(numbers)
if n in numbers:
    while left != right:
        mid = (left + right)//2
        if n == numbers[mid]:
            print("{0} at {1}".format(n, mid))
            break
        elif n < numbers[mid]:
            right = mid
        else:
            left = mid
else:
    print("Not Found")
