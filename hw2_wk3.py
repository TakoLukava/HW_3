import re
print(min((x for x in re.findall(r'\w+', input('enter:'))), key = len))

