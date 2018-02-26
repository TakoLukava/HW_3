i = 0
n = input('Enter the range of numbers: ')
_list = list(n)
ln = len(_list)


while i <= ln-1:
   if _list[i] == '0':
       _list.remove('0')
       _list.append(-1)
       i -= 1
   i += 1
print(_list)
