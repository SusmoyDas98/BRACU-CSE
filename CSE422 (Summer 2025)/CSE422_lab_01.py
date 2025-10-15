# PART 1

import heapq
def heuristic(x1,y1, x2, y2):
    answer = abs(x1-x2)+abs(y1-y2)
    return answer
def maze_solver(start_row, start_col, end_row, end_col):
    queue = []
    heapq.heappush(queue, (heuristic(start_row, start_col, end_row, end_col), (start_row, start_col,"")))
    visited = set()
    path = []
    cost_from_start[start_row][start_col] = 0
    while queue:
        current_h, current_node = heapq.heappop(queue)
        if current_node in visited : continue
        visited.add(current_node)
        c_row, c_col, direction = current_node
        path.append(direction)
        if c_row == end_row and c_col == end_col:
            break
        try:
            n_row, n_col = c_row+1, c_col
            if maze[n_row][n_col] == "0":
                n_distance = cost_from_start[c_row][c_col]+1
                if n_distance < cost_from_start[n_row][n_col]:
                    cost_from_start[n_row][n_col] = n_distance
                    n_f_x = n_distance + heuristic(n_row, n_col, end_row, end_col)
                    heapq.heappush(queue, (n_f_x, (n_row, n_col, "D")))
                    parent[n_row][n_col] = ((c_row, c_col),"D")
        except : pass
        try:
            n_row, n_col = c_row-1, c_col
            if maze[n_row][n_col] == "0":
                n_distance = cost_from_start[c_row][c_col]+1
                if n_distance < cost_from_start[n_row][n_col]:
                    cost_from_start[n_row][n_col] = n_distance
                    n_f_x = n_distance + heuristic(n_row, n_col, end_row, end_col)
                    heapq.heappush(queue, (n_f_x, (n_row, n_col,"U")))
                    parent[n_row][n_col] = ((c_row, c_col),"U")
        except : pass
        try:
            n_row, n_col = c_row, c_col+1
            if maze[n_row][n_col] == "0":
                n_distance = cost_from_start[c_row][c_col]+1
                if n_distance < cost_from_start[n_row][n_col]:
                    cost_from_start[n_row][n_col] = n_distance
                    n_f_x = n_distance + heuristic(n_row, n_col, end_row, end_col)
                    heapq.heappush(queue, (n_f_x, (n_row, n_col, "R")))
                    parent[n_row][n_col] = ((c_row, c_col),"R")
        except : pass
        try:
            n_row, n_col = c_row, c_col-1
            if maze[n_row][n_col] == "0":
                n_distance = cost_from_start[c_row][c_col]+1
                if n_distance < cost_from_start[n_row][n_col]:
                    cost_from_start[n_row][n_col] = n_distance
                    n_f_x = n_distance + heuristic(n_row, n_col, end_row, end_col)
                    heapq.heappush(queue, (n_f_x, (n_row, n_col, "L")))

                    parent[n_row][n_col] = ((c_row, c_col),"L")
        except : pass

    goal_row, goal_col = end_row, end_col

    total_path = ''

    while parent[goal_row][goal_col] != float("inf"):
        parent_node, direction = parent[goal_row][goal_col]
        total_path += direction
        goal_row, goal_col = parent_node

    if cost_from_start[end_row][end_col] == float("inf"):

        return '-1'

    return f"{cost_from_start[end_row][end_col]}\n{total_path[-1::-1]}"


with open('input1.txt',"r") as file1, open('output1.txt', 'w') as file2 :
    n, m = map(int, file1.readline().strip().split())
    a, b = map(int, file1.readline().strip().split())
    c, d = map(int, file1.readline().strip().split())
    maze = []
    cost_from_start = []
    parent = []
    for i in range(n):
        row = file1.readline().strip()
        temp = []
        cost = []
        prnt = []
        for j in row:
            temp.append(j)
            cost.append(float("inf"))
            prnt.append(float("inf"))
        maze.append(temp)
        cost_from_start.append(cost)
        parent.append(prnt)
    file2.write(maze_solver(a, b, c, d))


#-------------------------------------------------------------------------------------------------------------------


# PART 2

from collections import deque

def shortest_path_algorithm(start, end):
    queue = deque([])
    visited = []
    parent = [-1 for i in range(len(adj_list))]
    path_cost = [0 for i in range(len(adj_list))]
    color = [0 for i in range(len(adj_list))]
    queue.append(start); color[start] += 1
    while (queue):
        current_node = queue.popleft()
        visited.append(current_node)
        for i in range(len(adj_list[current_node])):
            child_node = adj_list[current_node][i]
            if color[child_node] == 0:
                color[child_node] += 1; queue.append(child_node)
                parent[child_node] = current_node; path_cost[child_node]+=1+path_cost[current_node]

    return path_cost[end]

def Admissibility_checker(adj_list, goal_node, heuristics):

    statement = True

    inadmissible_nodes = []

    for i in range(1,len(adj_list)):

        actual_value = shortest_path_algorithm(i, goal_node)
        if (actual_value < heuristics[i]):
            statement = False
            inadmissible_nodes.append(str(i))

    return (True, []) if statement == True else (False, inadmissible_nodes)



with open('input2.txt','r') as file1 , open('output2.txt', 'w') as file2:

    n, m  = map(int, file1.readline().strip().split())

    a, b = map(int, file1.readline().strip().split())

    adj_list = [[] for i in range(n+1)]

    heuristics  = [-1 for i in range(n+1)]

    for i in range(n):
        x,y = map(int, file1.readline().strip().split())
        heuristics[x] = y

    for i in range(m):
        u, v = map(int, file1.readline().strip().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    if Admissibility_checker(adj_list, b, heuristics)[0] == True:
        file2.write("1")
    else:
        inadmissible_nodes = Admissibility_checker(adj_list, b, heuristics)[1]

        file2.write(f"{0}\nHere nodes {','.join(inadmissible_nodes)} are inadmissible.")
