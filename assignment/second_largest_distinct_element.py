number=[12,35,1,10,34,35]
largest=None
second_largest=None

for num in number:
    if largest is None or num>largest :
        second_largest=largest
        largest=num
    elif num !=largest and (second_largest is None or num > second_largest):
        second_largest=num
if second_largest is None:
        print("no second largest distinct number")
else:
        print(second_largest)
