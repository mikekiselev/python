N = int(input())
j = 1
key = 0
while key < N:
    for i in range(j) :
        print(j, end=' ')
        key +=1
        if(key == N) :
            break
    j+=1