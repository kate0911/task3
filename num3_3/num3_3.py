import re
def route(field, cur_position, cur_route, steps,finish):
    cur_i , cur_j = cur_position
    
    if cur_position == finish:
        print(finish)
        return cur_route
    if steps == len(field)*len(field)/2 + len(field) + 1:
        return  cur_route
    
    if cur_i > 0 and field[cur_i - 1][cur_j] != 'п':
        route_up = route(field, (cur_i - 1, cur_j), cur_route + ['up'], steps + 1,finish)
        route_up_size = len(route_up)
    else:
        route_up_size = 1e10
        
    if cur_i < len(field) - 1 and field[cur_i + 1][cur_j] != 'п':
        route_down = route(field, (cur_i + 1, cur_j), cur_route + ['down'], steps + 1, finish)
        route_down_size = len(route_down)
    else:
        route_down_size = 1e10
        
    if cur_j > 0 and field[cur_i][cur_j - 1] != 'п':
        route_left = route(field, (cur_i, cur_j - 1), cur_route + ['left'], steps + 1,finish)
        route_left_size = len(route_left)
    else:
        route_left_size = 1e10
        
    if cur_j < len(field) - 1 and field[cur_i][cur_j + 1] != 'п':
        route_right = route(field, (cur_i, cur_j + 1), cur_route + ['right'], steps + 1,finish)
        route_right_size = len(route_right)
    else:
        route_right_size = 1e10
    
    if route_right_size == min(route_right_size,route_left_size,route_up_size,route_down_size,finish):
        return route_right

    if route_left_size == min(route_right_size,route_left_size,route_up_size,route_down_size,finish):
        return route_left
    
    if route_up_size == min(route_right_size,route_left_size,route_up_size,route_down_size):
        return route_up
    
    if route_down_size == min(route_right_size,route_left_size,route_up_size,route_down_size):
        return route_down

f = open('text.txt', 'r',encoding='utf-8')
file_list = re.split('\n', f.read())[:-1]

print(file_list)
finish=0,0
start=0,0
for i in range(len(file_list)):
    for j in range(len(file_list)):
        if file_list[i][j] == 'н':
            start = i, j
        if file_list[i][j] == 'к':
            finish = i, j
putb =  route(file_list, start, [], 0,finish)
if len(putb) == len(file_list)*len(file_list)/2 + len(file_list) + 1:
    print('no route')
else:
    print(putb)
