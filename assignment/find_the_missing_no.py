
number = [1, 2, 4, 6, 3, 7, 8]
n = 8

total = 0
for i in range(1, n + 1):
    total += i
sum_number = 0
for num in number:
    sum_number += num

missing = total - sum_number
print("Missing number:", missing)
