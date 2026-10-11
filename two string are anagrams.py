first = "listen"
second = "silent"

def are_anagrams(first, second):
    first = first.replace(" ", "").lower()
    second = second.replace(" ", "").lower()

    if len(first) != len(second):
        return False

    frequency = {}

    for char in first:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    for char in second:
        if char not in frequency:
            return False

        frequency[char] -= 1

        if frequency[char] < 0:
            return False

    return True

print(are_anagrams(first, second))

