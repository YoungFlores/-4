a = [1,2,3,5,34,2,1,44,12,4,124]
b = []
for i in range(len(a)):
    if a[i] > a[i-1]:
        b.append(a[i])
print(b)

