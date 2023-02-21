from math import *

file = open('text.txt', 'r')
lines = file.readlines()
file.close()

str_s = '+-*/'
sum1 = ''
for line in lines:
    for i in range(len(line) - 1):
        if line[i] in str_s and i == len(line) - 2:
            continue
        if line[i] == '^':
            sum1 += '**'
            continue
        if line[i] == 'n' and line[i - 1] == 'l':
            sum1 += 'og'
            continue
        sum1 += line[i]

print(sum1)
print(eval(sum1))

