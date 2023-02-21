import re


f = open('text.txt', 'r',encoding='utf-8')

your_string = f.read()
your_string = re.sub('\n', '', your_string)
to_del = []
a = re.split(r'\W+',re.sub('-', '', your_string))
print(a)
for elem, i  in zip(a, range(len(a))):
    b = (a *1)
    b.pop(i)
    if elem[::-1] in b:
        to_del.append(elem)
 
for elem in to_del:
    a.remove(elem)
print(a)

d = open('text.txt', 'w',encoding='utf-8')

for i in a:
    d.write(i + ' ')

f.close()
d.close()
