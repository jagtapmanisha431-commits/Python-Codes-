def duplicates(a):
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                return True
    return False

print(duplicates([1, 2, 3, 4, 2]))
