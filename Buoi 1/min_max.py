numbers = [10, 4 ,6, 18, 1000, 16, 3, 2, -10]
min1 = numbers[0]
for i in numbers:
    if i < min1:
        min1 = i
print("Min = ",min1)

max1 = numbers[0]
for i in numbers:
    if i > max1:
        max1 = i
print("Max = ", max1)
