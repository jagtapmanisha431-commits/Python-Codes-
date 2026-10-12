def process_numbers(numbers):
    total = 0
    count = 0
    largest = None

    for num in numbers:
        # Ignore negative numbers
        if num < 0:
            continue

        if num % 2 == 0:
            squared = num * num
            total += squared
            count += 1
            if largest is None or squared > largest:
                largest = squared

    if count == 0:
        return total, count, None

    return total, count, largest

numbers = [-2, 1, 2, 3, 4, 6, -8]
total, count, largest = process_numbers(numbers)

print("Total:", total)
print("Count:", count)
print("Largest squared value:", largest)
