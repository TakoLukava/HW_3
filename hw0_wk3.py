l=[]
counter = 0

while True:
    n= input('Enter a num:')
    if n=='':
        break
    l.append(int(n))


num= int(input('Enter num to count:'))

for n in l:
    if n == num:
        counter += 1
print('Count:{}').format(counter)
