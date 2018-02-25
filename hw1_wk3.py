import string
s=input('enter a word:')
for l in s[0]:
    if l in string.ascii_letters or l is '_':
        print ('true')

    else:
        break

        

