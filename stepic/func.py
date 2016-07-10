def modify_list(a):
    i= 0
    while  i <len(a):
        if a[i]%2 == 0 :
            a[i] = int(a[i]/2)
            i += 1
        else:
            del a[i]
    return

def modify_list1(a):
    for i in range(len(a)):
        if a[i]%2 == 0 :
            a[i] = int(a[i]/2)
            i += 1
        else:
            del a[i]
    return

a = [5,4, 6, 7, 9, 12, 13]
for i in a:
    print(i, end=' ')

print()
modify_list1(a)
print('--')
for i in a:
    print(i, end=' ')

print()