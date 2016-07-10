a = [int(i) for i in input().split()]
if len(a) == 1:
    print(a[0])
    quit()
print(a[1]+ a[-1], end = ' ')

for i in range(1, len(a)-1):
    print(a[i-1] + a[i+1], end=' ')

print(a[0]+a[-2], end = ' ')

print()