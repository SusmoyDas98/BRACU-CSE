'''   Lab Assignment 04  '''

''' Task 1 '''

'''Graph Representation'''

''' (A) '''

'''Adjoint matrix'''

with open("input1a.txt",'r') as file1, open('output1a.txt','w') as file2:
    N, M = map(int,file1.readline().strip().split())
    adj_matrix = [[0 for i in range(N+1)] for i in range(N+1)]
    for i in range(M):
        u, v, w =  map(int, file1.readline().strip().split())
        adj_matrix[u][v] = w
    for i in adj_matrix:
        for j in i:
            file2.write(f"{j} ")
        file2.write("\n")

#------------------------------------------------------------------------------------------------------------------------------


''' (B) '''

'''Adjoint List'''

'''USING LIST'''

with open("input1b.txt",'r') as file1, open('output1b.txt','w') as file2:
    N, M = map(int,file1.readline().strip().split())
    adj_list = [[] for i in range(N+1)]
    for i in range(M):
        u, v, w =  map(int, file1.readline().strip().split())
        adj_list[u].append((v,w))
    for i in range(len(adj_list)):
        file2.write(f"{i} : ")
        for j in adj_list[i]:
            file2.write(f"{j} ")
        file2.write("\n")

'''Brainstorming

a) If it was an undirected Graph, we had to add the w in the v column of u row and write the same value in u column of the v row of the Adjacency Matrix.
In case of the Adjacency List we add to append the (v,w) in u index of the list and append (u,w) in the v index of the list. Because, for every edge we can travel both ways as the graph would be undirected.

b) If we have parallel edges we cannot express the graph using the Adjacency Matrix. Becasue at each adj_list[u][v] it can only store one value.'''


#------------------------------------------------------------------------------------------------------------------------------


''' (B) '''

'''USING DICTIONARY'''

with open("input1b.txt",'r') as file1, open('output1b.txt','w') as file2:
    N, M = map(int,file1.readline().strip().split())
    adj_list = {}
    for i in range(N+1):
        adj_list[i] = []
    for i in range(M):
        u, v, w =  map(int, file1.readline().strip().split())
        adj_list[u].append((v,w))
    for k, v in adj_list.items():
        file2.write(f"{k} : ")
        for j in v:
            file2.write(f"{j} ")
        file2.write("\n")

#------------------------------------------------------------------------------------------------------------------------------

''' Task 2 '''

'''Graph Traversal Using BFS'''

from collections import deque
def BFS(source):
    queue = deque([])
    visited = []
    color = [0 for i in range(len(adj_list))]
    queue.append(source)
    color[source] += 1
    while len(queue) != 0:
        val = queue.popleft()
        visited.append(val)
        for i in range(len(adj_list[val])):
            if color[adj_list[val][i]] == 0:
                color[adj_list[val][i]] += 1
                queue.append(adj_list[val][i])
    return visited


with open("input2.txt",'r') as file1, open('output2.txt','w') as file2:
    N, M = map(int,file1.readline().strip().split())
    adj_list = [[] for i in range(N+1)]
    for i in range(M):
        u, v =  map(int, file1.
        readline().strip().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    source = 1
    result = BFS(source)
    for i in result:
        file2.write(f"{i} ")

'''TIME COMPLEXITY O(N+M)'''

#------------------------------------------------------------------------------------------------------------------------------

''' Task 3 '''

'''Graph Traversal Using DFS'''


def DFS(source):
    visited.append(source)
    color[source] += 1
    for i in range(len(adj_list[source])):
        if color[adj_list[source][i]] == 0 :
            DFS(adj_list[source][i])


with open("input3.txt",'r') as file1, open('output3.txt','w') as file2:
    N, M = map(int,file1.readline().strip().split())
    adj_list = [[] for i in range(N+1)]
    for i in range(M):
        u, v =  map(int, file1.
        readline().strip().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    source = 1

    visited = []
    color = [0 for i in range(len(adj_list))]
    DFS(source)
    for i in visited:
        file2.write(f"{i} ")

'''TIME COMPLEXITY O(N+M)'''

#------------------------------------------------------------------------------------------------------------------------------

'''  Task  4 '''

'''Cycle Finding'''

def cycle_finder(source):
    color[source] = 1
    for i in range(len(adj_list[source])):
        if color[adj_list[source][i]] == 0 :
            cycle_finder(adj_list[source][i])
        elif color[adj_list[source][i]] == 1 :
            global cycle
            cycle = True
            return
    color[source] = 2

with open("input4.txt",'r') as file1, open('output4.txt','w') as file2:
    N, M = map(int,file1.readline().strip().split())
    adj_list = [[] for i in range(N+1)]
    for i in range(M):
        u, v =  map(int, file1.readline().strip().split())
        adj_list[u].append(v)
    source = 1
    cycle = False
    color = [0 for i in range(len(adj_list))]
    cycle_finder(source)
    if cycle == True:
        file2.write(f"YES")
    else:
        file2.write(f"NO")


'''TIME COMPLEXITY O(N+M)'''

'''Brainstorming
a) Yes.
b) Yes, by checking if the given graph is a bipartite graph or not.'''


#------------------------------------------------------------------------------------------------------------------------------


'''  Task 5 '''

'''Find the shortest path'''


from collections import deque
def shortest_path_finder(source):
    queue = deque([])
    queue.append(source)
    color[source] += 1
    while len(queue) != 0:
        u = queue.popleft()
        global D
        if u == D:
            return
        for i in adj_list[u]:
            if color[i] == 0:
                color[i] += 1
                parent[i] = u
                distance[i] += distance[u] + 1
                queue.append(i)


with open("input5.txt",'r') as file1, open('output5.txt','w') as file2:
    N, M, D = map(int,file1.readline().strip().split())
    adj_list = [[] for i in range(N+1)]
    for i in range(M):
        u, v =  map(int, file1.readline().strip().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    color = [0 for i in range(len(adj_list))]
    parent = [0 for i in range(len(adj_list))]
    distance = [0 for i in range(len(adj_list))]
    source = 1
    shortest_path_finder(source)
    i = D
    path = ""
    while parent[i] > 0 :
        path += str(i)+" "
        i = parent[i]
    path += str(source)
    file2.write(f"Time: {distance[D]}\nShortest Path: {path[-1::-1]}")


'''TIME COMPLEXITY O(N+M)'''

#------------------------------------------------------------------------------------------------------------------------------


'''  Task 6 '''

'''Flood Fill'''


def Diamond_collector_using_BFS(i,j):
    from collections import deque
    queue = deque([])
    paths = [[-1,-1],[-1,+1],[-1,0],[0,+1],[0,-1],[1,0],[1,-1],[1,1]]
    queue.append((i,j))
    count = 0
    while len(queue) != 0:
        x,y = queue.popleft()
        if grid[x][y]  == "D":
            count += 1

        for i in range(len(paths)):
            a, b = paths[i][0]+x,paths[i][1]+y

            if 0<=a<N and 0<=b<M:
                if visited[a][b] == 0:
                    if grid[a][b]  == "." or grid[a][b]  == "D":
                            visited[a][b] = 1
                            queue.append((a,b))

    return count

with open("input6.txt",'r') as file1, open('output6.txt', 'w') as file2:
    N,M = map(int, file1.readline().strip().split())
    grid = []
    visited = []
    lst2 = []
    for  i in range(N):
        lst = [j for j in file1.readline().strip()]

        lst2 = [0 for k in range(len(lst))]
        visited.append(lst2)
        grid.append(lst)

    Diamonds = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == "." and visited[i][j] == 0:
                Diamonds = max(Diamond_collector_using_BFS(i,j), Diamonds)
    file2.write(Diamonds)


'''TIME COMPLEXITY O(NM)'''


#------------------------------------------------------------------------------------------------------------------------------


'''  Task 7  '''


def longest_path_finder(source):
    from collections import deque
    queue = deque([])
    color = [0 for i in range(len(adj_list))]
    distance = [0 for i in range(len(adj_list))]
    queue.append(source)
    distance[source] = 0
    while len(queue) != 0:
        u = queue.popleft()
        color[u] += 1
        for i in range(len(adj_list[u])):
            if color[adj_list[u][i]] == 0:
                queue.append(adj_list[u][i])
                distance[adj_list[u][i]] = distance[u]+1

    return distance.index(max(distance))


with open("input7.txt",'r') as file1, open('output7.txt','w') as file2:
    N = list(map(int,file1.readline().strip().split()))
    N = N[0]
    adj_list = [[] for i in range(N+1)]
    for i in range(N-1):
        u, v =  map(int, file1.readline().strip().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    source1 = longest_path_finder(1)
    destination1 = longest_path_finder((source1))
    file2.write(f"{source1} {destination1}")


'''TIME COMPLEXITY O(N)'''

#------------------------------------------------------------------------------------------------------------------------------


''' Task 8 '''


def bipartite(source):
    from collections import deque
    queue = deque([])
    visited = [0 for i in range(len(adj_list))]
    queue.append(source)
    color = [None for i in range(len(adj_list))]
    parent = [None for i in range(len(adj_list))]
    color[source] = True
    while len(queue) != 0:
        u = queue.popleft()
        visited[u] = 1
        for i in  range(len(adj_list[u])):
            if visited[adj_list[u][i]] == 0:

                color[adj_list[u][i]] = not color[u]
                queue.append(adj_list[u][i])
            else:
                if color[u] == color[adj_list[u][i]]:
                    return False

    return max(color.count(True), color.count(False))

with open('input8.txt', 'r') as file1, open("output8.txt","w")  as file2:
    N = int(file1.readline().strip())

    for i in range(N):
        M = int(file1.readline().strip())
        adj_list = [[] for  i in range(M+2)]

        for j in range(M):
                u,v = map(int, file1.readline().strip().split())
                adj_list[u].append(v)
                adj_list[v].append(u)


        file2.write(f"Case {i+1}: {bipartite(1)}\n")


'''TIME COMPLEXITY O(N+M)'''


#------------------------------------------------------------------------------------------------------------------------------


''' Task 9 '''

'''A (USING DFS)'''

def sequence_maker_DFS(source):
    color[source] = 1
    visited.append(source)
    for i in range(len(adj_list[source])):
        if color[adj_list[source][i]]==1:
            return
        elif color[adj_list[source][i]]==0:
            in_degree[adj_list[source][i]] -= 1
            if in_degree[adj_list[source][i]] == 0:
                sequence_maker_DFS(adj_list[source][i])
    color[source] = 2

with open('input9a.txt','r') as file1, open('output9a.txt','w') as file2:
    N,M = map(int, file1.readline().strip().split())
    in_degree = [0 for i in range(N+1)]
    adj_list = [[] for i in range(N+1)]
    for i in range(M):
        u, v = map(int,file1.readline().strip().split())
        adj_list[u].append(v)
        in_degree[v] += 1
    visited = []
    status = True
    color = [0 for i in range(N+1)]

    for i in range(1,len(in_degree)):
            if in_degree[i] == 0 and  color[i] == 0:

                sequence_maker_DFS(i)
    if len(visited) != N:
        file2.write("IMPOSSIBLE")
    else:
        for i in visited:
            file2.write(f"{i} ")

'''TIME COMPLEXITY O(N+M)'''


#------------------------------------------------------------------------------------------------------------------------------




'''B (Unsing BFS)'''

def sequence_maker_BFS(source):
    from collections import deque
    queue = deque([])
    queue.append(source)
    while len(queue) != 0 :
        u = queue.popleft()
        visited.append(u)
        for i in range(len(adj_list[u])):
            in_degree[adj_list[u][i]] -= 1
            if in_degree[adj_list[u][i]] == 0:
                queue.append(adj_list[u][i])

with open('input9b.txt','r') as file1, open('output9b.txt','w') as file2:
    N,M = map(int, file1.readline().strip().split())
    in_degree = [0 for i in range(N+1)]
    adj_list = [[] for i in range(N+1)]
    for i in range(M):
        u, v = map(int,file1.readline().strip().split())
        adj_list[u].append(v)
        in_degree[v] += 1
    visited = []

    for i in range(len(in_degree)):
        if in_degree[i] == 0 and i>0 and i not in visited:
            sequence_maker_BFS(i)
    if len(visited) != N:
        file2.write("IMPOSSIBLE")
    else:
        for i in visited:
            file2.write(f"{i} ")

'''TIME COMPLEXITY O(N+M)'''


#------------------------------------------------------------------------------------------------------------------------------


''' Task 10 '''


def lexicographic_sequence_maker_BFS(source):
    import heapq
    queue = []
    heapq.heappush(queue, source)
    while len(queue) != 0 :
        u = heapq.heappop(queue)
        visited.append(u)
        for i in range(len(adj_list[u])):
            in_degree[adj_list[u][i]] -= 1
            if in_degree[adj_list[u][i]] == 0:
                heapq.heappush(queue, adj_list[u][i])

with open('input10.txt','r') as file1, open('output10.txt','w') as file2:
    N,M = map(int, file1.readline().strip().split())
    in_degree = [0 for i in range(N+1)]
    adj_list = [[] for i in range(N+1)]
    for i in range(M):
        u, v = map(int,file1.readline().strip().split())
        adj_list[u].append(v)
        in_degree[v] += 1
    visited = []

    for i in range(len(in_degree)):
        if in_degree[i] == 0 and i>0 and i not in visited:
            lexicographic_sequence_maker_BFS(i)
    if len(visited) != N:
        file2.write("IMPOSSIBLE")
    else:
        for i in visited:
            file2.write(f"{i} ")

'''TIME COMPLEXITY O((N+M)logN)'''

