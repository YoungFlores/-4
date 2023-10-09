a = [1,2,3,4,5,6]
b = [8,45,3,4,5,6]
count = 0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            count += 1

print(count)

