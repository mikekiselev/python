a = [int(i) for i in input().split()]
a.sort()

i = 0;
N = len(a)
while i < N:
    klv = a.count(a[i])
    if klv > 1 :
        print(a[i], end= ' ')
    i = i + klv