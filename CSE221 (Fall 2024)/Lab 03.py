#Task 1
def merge(a, b):
    i, j = 0, 0
    final = []
    while i<len(a) or j<len(b):
        if i >= len(a)  and j<len(b):
            final.append(b[j])
            j+=1
        elif j>=len(b) and i<len(a):
            final.append(a[i])
            i+=1
        elif a[i] <= b[j] :
            final.append(a[i])
            i+=1
        elif b[j]<a[i]:
            final.append(b[j])
            j+=1
    return final
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)

with open('input1.txt', 'r') as file1,open('output1.txt','w') as file2:
    N, lst = file1.readlines()
    lst = [int(i) for i in lst.strip().split()]
    lst1 = mergeSort(lst)
    for i in lst1:
        file2.write(f"{i} ")


#Task 2
def maximum(arr):
    if len(arr) <= 1:
        return arr[0]
    mid = len(arr)//2
    left_val = maximum(arr[:mid])
    right_val = maximum(arr[mid:])
    return max(left_val, right_val)

with open('input2.txt', 'r') as file1,open('output2.txt','w') as file2:
    N, lst = file1.readlines()
    lst = [int(i) for i in lst.strip().split()]
    largest = maximum(lst)
    file2.write(f"{largest[0]}")

# The Time Complexity of this code is O(n)


#Task 3
def counter(a, b):
    i, j = 0, 0
    final = []
    while i<len(a) or j<len(b):
        if i >= len(a)  and j<len(b):
            final.append(b[j])
            j+=1
        elif j>=len(b) and i<len(a):
            final.append(a[i])
            i+=1
        elif a[i] <= b[j] :
            final.append(a[i])
            i+=1
        elif b[j]<a[i]:
            global count
            count += len(a)-i
            final.append(b[j])
            j+=1
    return final

def finder(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = finder(arr[:mid])
        a2 = finder(arr[mid:])
        return counter(a1, a2)

with open('input3.txt', 'r') as file1,open('output3.txt','w') as file2:
    N, lst = file1.readlines()
    lst = [int(i) for i in lst.strip().split()]
    count = 0
    lst1 = finder(lst)
    file2.write(f"{count}")

#Task 4
def value_finder(arr1, arr2):
    i,j = 0,0
    while i<len(arr1) and j<len(arr2):
        a = arr1[i] + arr2[j]**2
        global value
        value = max(value,a)
        if arr1[i]<=arr2[j]:
            i+=1
        else:
            j+=1
    return arr1+arr2
def maximizer(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    a1 = maximizer(arr[:mid])
    a2 = maximizer(arr[mid:])
    return value_finder(a1,a2)
with open('input4.txt', 'r') as file1,open('output4.txt','w') as file2:
    import math
    N, lst = file1.readlines()
    arr = [int(i) for i in lst.strip().split()]
    value = -math.inf
    maximizer(arr)
    file2.write(f"{value}")

#Task 5
def partition(arr, start, end):
    pivot = arr[end]
    indx = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[indx], arr[i] = arr[i], arr[indx]
            indx+=1
    arr[end],arr[indx] = arr[indx],arr[end]
    return indx
def quick_sort(arr, start, end):
    if start<end:
        indx = partition(arr, start, end)
        quick_sort(arr, start, indx-1)
        quick_sort(arr, indx+1, end )
with open('input5.txt', 'r') as file1,open('output5.txt','w') as file2:
    N, lst = file1.readlines()
    arr = [int(i) for i in lst.strip().split()]
    quick_sort(arr, 0, int(N)-1)
    for i in arr:
        file2.write(f"{i} ")


#Task 6
def partition(arr, start, end):
    pivot = arr[end]
    indx = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[indx], arr[i] = arr[i], arr[indx]
            indx+=1
    arr[end],arr[indx] = arr[indx],arr[end]
    return indx
def kth_finder(arr, n, start, end):
    indx =  partition(arr, start, end)
    if indx == n:
        return arr[indx]
    elif indx > n:
        return kth_finder(arr, n, start, indx-1)
    elif indx < n:
        return kth_finder(arr,n, indx+1, end)

with open('input6.txt', 'r') as file1,open('output6.txt','w') as file2:
    N, arr, M, *num = file1.readlines()
    arr =  [int(i) for i in arr.split()]
    num = [int(i.strip()) for i in num]
    for i in num:
        file2.write(f"{kth_finder(arr,i-1, 0, len(arr)-1)}\n")
