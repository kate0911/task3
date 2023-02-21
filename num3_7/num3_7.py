import re
f = open('text.txt', 'r',encoding='utf-8')
text=f.read()
TEXT=list(text)
dict={}
for i in range (0,len(TEXT)):
    if TEXT[i] in dict:
        dict[TEXT[i]]+=1
    else:
        dict[TEXT[i]]=1
for i in dict:
    if(dict[i]==2):
        print(i)
    
