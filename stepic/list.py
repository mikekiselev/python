a = [int(i) for i in input().split()]
if len(a) == 1:
    print(a[0])
    quit()
for i in range(0, len(a)):
    if i == 0:
        x = a[-1]
        y = a[1]
        print(y+ x, end = ' ')
        continue
    if i == len(a)-1 :
        print(a[0]+a[-2], end = ' ')
        break
    print(a[i-1]+a[i+1], end = ' ')
print()
