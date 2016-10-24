N = int(input('input N= '))

a = [[i+j+1 for i in range(N)] for j in range(N)]

for i in range(N):
    for j in range(N):
        print( a[i][j], end=' ')
    print()
