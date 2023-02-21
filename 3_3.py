#nu3
import re


def route(field, cur_position,pred_position, cur_route, steps, BESTpath):
    i,j = cur_i , cur_j = cur_position
    print(cur_position)
 
    if cur_position == finish:
        print("ura",cur_route )
        if(len(BESTpath)>len(cur_route) or len(BESTpath)==0):
            BESTpath=cur_route[::]
        return BESTpath
    if steps == len(field)*len(field)/2 + len(field) + 1:
        return  cur_route
    #если можем двигаться влево
    if cur_i > 0 and field[cur_i - 1][cur_j] != 'п' and pred_position!=(i-1,j):
        BESTpath = route(field, (cur_i - 1, cur_j),(i,j), cur_route + ['up'], steps + 1,BESTpath)
    #если можем двигаться вправо
    if cur_i < len(field) - 1 and field[cur_i + 1][cur_j] != 'п'and pred_position!=(i+1,j):
        BESTpath = route(field, (cur_i + 1, cur_j), (i,j), cur_route + ['down'], steps + 1,BESTpath)
   
    #если можем двигаться вверх

    if cur_j > 0 and field[cur_i][cur_j - 1] != 'п'and pred_position!=(i,j-1):
        BESTpath = route(field, (cur_i, cur_j - 1),(i,j), cur_route + ['left'], steps + 1,BESTpath)

    #если можем двигаться вниз

    if cur_j < len(field) - 1 and field[cur_i][cur_j + 1] != 'п' and pred_position!=(i,j+1):
        BESTpath = route(field, (cur_i, cur_j + 1), (i,j),cur_route + ['right'], steps + 1,BESTpath)
#     if(len(BESTpath)>len(route_right) and len(BESTpath)==0):
    
#     возвращаем путь с минимальной длиной
    return BESTpath

f = open('input3.txt', 'r', encoding='utf-8')
file_list = re.split('\n', f.read())[:-1]

print(file_list)
print(len(file_list))

for i in range(len(file_list)):
    for j in range(len(file_list)):
        
        if file_list[i][j] == 'н':
            start = i, j
        if file_list[i][j] == 'к':
            finish = i, j
print(start, finish)
putb =  route(file_list, start,(0,0), [], 0,[])

if len(putb) == len(file_list)*len(file_list)/2 + len(file_list) + 1 or len(putb) ==0:
    print('no route')
    file = open('output3.txt', 'w')
    file.write("no route")

    file.close()
else:
    print(putb)
    z=[]
    for x in file_list:
        z.append(list(x))

    s1 = start[0]
    s2 = start[1]
    for x in putb:
        if x == 'left':
            s2-=1
            if z[s1][s2] == '0' :
                z[s1][s2] = '*'
        if x == 'right':
            s1+=1
            if z[s1][s2] == '0' :
                z[s1][s2] = '*'
        if x == 'down':
            s1+=1
            if z[s1][s2] == '0' :
                z[s1][s2] = '*'
        if x == 'up':
            s1-=1
            if z[s1][s2] == '0' :
                z[s1][s2] = '*'


    file = open('output3.txt', 'w')
    for x in z:
        for y in x:
            file.write(y)
        file.write("\n")


    file.close()
