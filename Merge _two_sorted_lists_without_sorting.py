a =[1, 4, 7, 10]
b =[2, 3, 8, 11, 15]
i =0
j =0
result =[]

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1
result.extend(a[i:])
result.extend(b[j:])
print(result)