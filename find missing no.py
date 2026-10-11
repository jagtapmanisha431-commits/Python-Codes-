def find_missing(number, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = 0
    for num in number:
        actual_sum = actual_sum + num
    missing = expected_sum - actual_sum
    return missing

print(find_missing([1, 2, 4, 5], 5))
print(find_missing([2, 3, 4, 5], 5))
