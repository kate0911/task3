import re
f = open('text.txt', 'r',encoding='utf-8')
text=f.read()
print(text)
p=re.compile(r"[a-zA-Z-]+",re.S)
print("yes" if p.search(text) else "no")
match=[]
match=p.findall(text)
print(type(match))
for i in match:
    print(i)
    for j in match:
        if(i==j):
            del(i)
print (match)
