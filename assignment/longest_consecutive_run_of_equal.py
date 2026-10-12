number=[1,1,2,2,2,3,3,1,1,1,1]
max_count = 0
current_count = 1

for i in range(1, len(number)):
    if number[i]==number[i-1]:
        current_count+=1
    else:
        max_count=max(max_count, current_count)
        current_count=1
max_count=max(max_count, current_count)
print(max_count)