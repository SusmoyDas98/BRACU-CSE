''' Lab Assignment 05 '''

'''Task 1'''

def dijkstra_algorithm(source):
    import heapq
    import math
    queue = []
    color = [0 for i in range(len(adj_list))]
    distance = [math.inf for i in range(len(adj_list))]
    distance[source] = 0
    heapq.heappush(queue, (distance[source],source))
    while len(queue) != 0:
        weight, val =  heapq.heappop(queue)
        for i in range(len(adj_list[val])):
            a, w = adj_list[val][i]
            if color[a] == 0:
                if distance[a] > weight+ w:
                    distance[a] = weight+w
                    heapq.heappush(queue, (distance[a],a))

        color[val] = 1
    return distance

with open('input1.txt','r') as file1, open('output1.txt','w') as file2:
    N, M = map(int, file1.readline().strip().split())
    adj_list = [[] for  i in range(N+1)]
    for i in range(M):
        u,v,w = map(int, file1.readline().strip().split())
        adj_list[u].append((v,w))
    source = int(file1.readline().strip())
    results = dijkstra_algorithm(source)
    import math
    for i in range(1,len(results)):
        if results[i] == math.inf:
            file2.write(f"{-1} ")
        else: file2.write(f"{results[i] } ")

#------------------------------------------------------------------------------------------------------------------------------


'''Task 2'''


def dijkstra_algorithm(source):
    import heapq
    import math
    queue = []
    color = [0 for i in range(len(adj_list))]
    distance = [math.inf for i in range(len(adj_list))]
    distance[source] = 0
    heapq.heappush(queue, (distance[source],source))
    while len(queue) != 0:
        weight, val =  heapq.heappop(queue)
        for i in range(len(adj_list[val])):
            a, w = adj_list[val][i]
            if color[a] == 0:
                if distance[a] > weight+ w:
                    distance[a] = weight+w
                    heapq.heappush(queue, (distance[a],a))

        color[val] = 1
    return distance
with open('input2.txt','r') as file1, open('output2.txt','w') as file2:
    N,M = map(int, file1.readline().strip().split())
    adj_list = [[] for i in range(N+1)]
    for i in range(M):
        u,v,w = map(int, file1.readline().strip().split())
        adj_list[u].append((v,w))
    source1, source2 = map(int, file1.readline().strip().split())
    result1 = dijkstra_algorithm(source1)
    result2 = dijkstra_algorithm(source2)
    i = 0
    Time, Node = math.inf, 0
    status = False
    while i<len(result1) and i<len(result2):
        if result1[i] is not math.inf and result2[i] is not math.inf:
            if  max(result1[i], result2[i]) < Time:
                Time = max(result1[i], result2[i])
                Node = i
                status = True
        i+=1
    if not status : file2.write("Impossible")
    else: file2.write(f"Time {Time} \nNode {Node}")


#------------------------------------------------------------------------------------------------------------------------------


'''#Task 3'''


def minimum_danger(source):
    import heapq
    import math
    distance = [math.inf for i in range(len(adj_list))]
    color = [0  for i in range(len(adj_list))]
    distance[source] = 0
    queue = []
    heapq.heappush(queue, (distance[source], source))
    while len(queue) != 0:
        weight, value = heapq.heappop(queue)
        for i in range(len(adj_list[value])):
            V, W = adj_list[value][i]
            if color[V] == 0:
                if max(W, value) < distance[V]:
                    distance[V] = max(W, distance[value])
                    heapq.heappush(queue, (distance[V], V))
        color[value] = 1
    return distance


with open('input3.txt','r') as file1, open('output3.txt','w') as file2:
    N, M = map(int, file1.readline().strip().split())
    adj_list = [[] for i in range(N+1)]
    for  i in range(M):
        u,v,w = map(int, file1.readline().strip().split())
        adj_list[u].append((v,w))
    import math
    if minimum_danger(1)[N] == math.inf:
        file2.write("Impossible")
    else: file2.write(f"{minimum_danger(1)[N]}")


#------------------------------------------------------------------------------------------------------------------------------


'''Task 4'''


def find_parent(node):
    if parents[node] == node:
        return node
    return find_parent(parents[node])

def Union(node1, node2):
    parent_node1, parent_node2 = find_parent(node1), find_parent(node2)
    if parent_node1 == parent_node2: return  size[parent_node1]
    if size[parent_node1] < size[parent_node2]:
        parent_node1, parent_node2 = parent_node2, parent_node1
    parents[parent_node2] = parent_node1
    size[parent_node1] += size[parent_node2]
    return size[parent_node1]
def friends_counter(arr):
    for i in range(1, len(arr)):
        a, b = arr[i]
        file2.write(f"{Union(a,b)}\n")


with open('input4.txt','r') as file1, open('output4.txt','w') as file2:
    N,M = map(int, file1.readline().strip().split())
    friends = [0]
    for i in range(M):
        a,b = map(int, file1.readline().strip().split())
        friends.append((a,b))
    parents = [i for i in range(N)]

    size = [1 for i in range(N)]
    friends_counter(friends)





#------------------------------------------------------------------------------------------------------------------------------


'''Task 5'''


def find_parent(node):
    if parent[node] == node: return node
    return find_parent(parent[node])

def union(node1, node2):
    parent1, parent2 = find_parent(node1), find_parent(node2)
    if parent1 == parent2:
        return False
    if size[parent1] < size[parent2]:
        parent1, parent2 = parent2, parent1
    parent[parent2] = parent1
    size[parent1] += size[parent2]
    return True
def Kruskal_algorithm(arr):
    import heapq
    while len(arr) > 0:
        cost, (point1, point2) = heapq.heappop(arr) 
        if union(point1,point2) :
            global total_cost
            total_cost += cost


with open('input5.txt','r') as file1, open('output5.txt','w') as file2:
    N,M = map(int, file1.readline().strip().split())
    import heapq
    adj_list = []
    for i in range(M):
        u, v, w = map(int, file1.readline().strip().split())
        heapq.heappush(adj_list,(w,(u,v)))
    parent = [i for i in range(N+1)]
    size = [1 for i  in range(N+1)]
    total_cost = 0
    Kruskal_algorithm(adj_list)
    print(total_cost)
    

