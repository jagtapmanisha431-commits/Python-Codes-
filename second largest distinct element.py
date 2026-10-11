def second_largest(numbers):
    largest = None
    second = None

    for num in numbers:
        if largest is None or num > largest:
            second = largest
            largest = num
        elif num != largest and (second is None or num > second):
            second = num

    if second is None:
        return "No second-largest distinct value"

    return second


numbers = [10, 20, 5, 15, 20]
print(second_largest(numbers))
