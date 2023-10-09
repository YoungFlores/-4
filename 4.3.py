array = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
counts = {}

for i in array:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

for count in counts.values():
    print(count, end=' ')