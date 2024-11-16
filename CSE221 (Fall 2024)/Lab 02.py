#Lab Assignment 2
#Task 1
with  open('input1.txt','r') as file1, open('output1.txt', 'w') as file2:
    N, S = map(int, file1.readline().strip().split(" "))
    lst = list(map(int, file1.readline().strip().split()))
    i, j = 0, len(lst)-1
    found = False
    while i<j:
        if lst[i] + lst[j] < S:
            i+=1

        elif lst[i] + lst[j] > S:
            j-=1
        elif lst[i] + lst[j] == S:
            file2.write(f"{i+1} {j+1}")
            found = True
            break
    if not found:
        file2.write(f"IMPOSSIBLE")

#Task 2
#A
with  open('input2.txt','r') as file1, open('output2.txt', 'w') as file2:
    arr = list(file1.readlines())
    l1,lst1, l2, lst2 = arr
    lst1, lst2 = lst1.split(), lst2.split()
    lst1, lst2 = [int(i) for i in lst1], [int(j) for j in lst2]
    final = lst1+lst2
    final.sort()
    final = [str(i) for i in final]

    file2.write(f"{' '.join(final)}")


#B
with  open('input2.txt','r') as file1, open('output2.txt', 'w') as file2:
    arr = list(file1.readlines())
    l1,lst1, l2, lst2 = arr
    lst1, lst2 = lst1.split(), lst2.split()
    lst1, lst2 = [int(i) for i in lst1], [int(j) for j in lst2]
    final = []
    i,j = 0, 0
    while i<int(l1) or j<int(l2):
        if i >= int(l1)  and j<int(l2):
            final.append(str(lst2[j]))
            j+=1
        elif j>=int(l2) and i<int(l1):
            final.append(str(lst1[i]))
            i+=1
        elif lst1[i] <= lst2[j] :
            final.append(str(lst1[i]))
            i+=1
        elif lst2[j]<lst1[i]:
            final.append(str(lst2[j]))
            j+=1
    file2.write(f"{' '.join(final)}")



#Task 3
with open('input3.txt','r') as file1, open('output3.txt','w') as file2:
    N = int(file1.readline().strip())
    dic, end = {},[]
    for i in range(N):
        a, b = map(int,file1.readline().strip().split())
        dic[b] = a
        end.append(b)
    end = sorted(end)
    added = [0]
    tasks = []
    for i in range(len(end)):
        if dic[end[i]] >= added[-1] :
            added.append(end[i])
            tasks.append(f"{dic[end[i]]} {end[i]}")
    file2.write(f"{len(added)-1}\n")
    for i in tasks:
        file2.write(f"{i} \n")

#Task 4
# A
import math
with open('input4.txt','r') as file1, open('output4.txt','w') as file2:
    N, M = map(int, file1.readline().strip().split())
    dic, end = {},[]
    for i in range(N):
        a, b = map(int,file1.readline().strip().split())
        dic[b] = a
        end.append(b)
    end = sorted(end)
    people = [0]*M
    count = 0
    for i in range(len(end)):
        diff = math.inf
        indx = None
        for j in range(M):
            if people[j] <= dic[end[i]] and (dic[end[i]]-people[j])<=diff :
                diff = (dic[end[i]]-people[j])
                indx = j
                found = True
        if indx!=None :
            people[indx] = end[i]
            count += 1
    file2.write(f"{count}")
