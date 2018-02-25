from random import random
N=10
a=[10,13,0,23,40,12]
l = int(input('Enter min number of strings: '))
h = int(input('enter max number of strings:  '))

for i in range(N):
    n=int(random()*(h-1)) + 1
    a.append(n)
print(a)

v=int(0|10)
i=0
m=N
while i < m:
    if a[i] == v:
        del a[i]
        m -= 1
    else:
        i += 1
for i in range(m,N):
    a.append(-1)
print(a)