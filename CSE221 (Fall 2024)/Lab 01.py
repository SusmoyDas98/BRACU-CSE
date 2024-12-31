''' Lab 01 '''
''' Task 1 '''


''' a'''
with open("input1a.txt", "r") as file1, open('output1a.txt', 'w') as file2:
    lines = file1.readlines()
    N = int(lines[0].strip())
    for i in range(1, N+1):
        current = int(lines[i].strip())
        if current % 2 == 0:
            file2.write(f"{current} is an Even number.\n")
        else:
            file2.write(f"{current} is an Odd number.\n")


''' b '''
with open('input1b.txt','r') as file1, open('output1b.txt', 'w') as file2:
    lines = file1.readlines()
    N = int(lines[0].strip())
    for i in range(1, N+1):
        lst  =  lines[i].split()
        if lst[2] == "+":
            file2.write(f"The result of {int(lst[1].strip())} + {int(lst[3].strip())} is {int(lst[1].strip())+int(lst[3].strip())}\n")
        elif lst[2] == "-":
            file2.write(f"The result of {int(lst[1].strip())} + {int(lst[3].strip())} is {int(lst[1].strip())-int(lst[3].strip())}\n")
        elif lst[2] == "*":
            file2.write(f"The result of {int(lst[1].strip())} + {int(lst[3].strip())} is {int(lst[1].strip())*int(lst[3].strip())}\n")
        elif lst[2] == "/":
            file2.write(f"The result of {int(lst[1].strip())} + {int(lst[3].strip())} is {int(lst[1].strip())/int(lst[3].strip())}\n")

#------------------------------------------------------------------------------------------------------------------------------


''' Task 2 '''

def bubbleSort(arr):
    for i in range(len(arr)-1):
        status = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                status = True
        if status == False: return
with open('input2.txt','r') as file1, open('output2.txt', 'w') as file2:
    N, arr = file1.readlines()
    arr = arr.split(" ")
    arr = list(map(int, arr))
    bubbleSort(arr)
    arr = list(map(str, arr))
    file2.write(f"{' '.join(arr)}")

#------------------------------------------------------------------------------------------------------------------------------


''' Task 3 '''

def selection_sort(arr1, arr2):
    for i in range(len(arr1)):
        current = i
        for j in range(i+1, len(arr1)):
            if arr1[j]>arr1[current] or (arr1[current] == arr1[j] and arr2[j]<arr2[current]):
                current = j
        arr1[i],arr2[i], arr1[current], arr2[current] = arr1[current], arr2[current], arr1[i],  arr2[i]
with open('input3.txt', 'r') as file1, open('output3.txt', 'w') as file2:
    N, arr1, arr2 = file1.readlines()
    arr1 = list(map(int, arr1.split(" ")))
    arr2 = list(map(int, arr2.split(" ")))
    selection_sort(arr2, arr1)
    for i in range(len(arr1)):
        file2.write(f"ID: {arr1[i]} Mark: {arr2[i]}\n")

#------------------------------------------------------------------------------------------------------------------------------


''' Task 4 '''

def sorting(arr):
    for i in range(len(arr)):
        current = i
        for j in range(i+1, len(arr)):
            if arr[j][0]<arr[current][0] or (arr[j][0] == arr[current][0] and arr[j][-1]>arr[current][-1]):
                current = j
        arr[i], arr[current] = arr[current], arr[i]

with open('input4.txt', 'r') as file1, open('output4.txt', 'w') as file2:
    N, *lst = file1.readlines()
    lst = [i.strip().split(" ") for i in lst]
    sorting(lst)
    for i in lst:
        file2.write(" ".join(i)+"\n")
