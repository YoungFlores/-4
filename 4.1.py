a = [1,32,132,33,22]
min = 999999999
max = 0
max_num = 0
min_num = 0
for i in range(len(a)):
    if a[i] <= min:
        min = a[i]
        min_num = i

    elif a[i] >= max:
        max = a[i]
        max_num = i
a[min_num],a[max_num] = a[max_num],a[min_num]
print(a)


