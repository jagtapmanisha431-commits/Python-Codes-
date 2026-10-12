first = "listen"
second = "silent"

if len(first) != len(second):
    print("false")
else:
    freq ={}
    for check in first:
        freq[check] = freq.get(check, 0) + 1
    for check in second:
        if check not in freq or freq[check] == 0:
            print("false")
            break
        freq[check] -= 1
    else:
        print("true")