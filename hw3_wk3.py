N=5
a = []
for i in range(N):
    print(i+1, end='-я: ')
    a.append(input())

ind = 0
for i in range(1,N):
    if len(a[i]) > len(a[ind]):
        ind = i

for i in range (N):
    if len(a[i]) == len(a[ind]):
        print(i+1)