import re
f = open('text.txt', 'r',encoding='utf-8')
text=f.read()
print(text)
p=re.compile(r"\b(\w*ккк\w*)\b",re.I)
print("yes" if p.search(text) else "no")
#match=[]
match=p.findall(text)
print (match)
