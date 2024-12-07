#Assignment 3

import numpy as np

#Run this cell
class Node:
  def __init__(self,elem,next = None):
    self.elem,self.next = elem,next

def createList(arr):
  head = Node(arr[0])
  tail = head
  for i in range(1,len(arr)):
    newNode = Node(arr[i])
    tail.next = newNode
    tail = newNode
  return head

def printLinkedList(head):
  temp = head
  while temp != None:
    if temp.next != None:
      print(temp.elem, end = '-->')
    else:
      print(temp.elem)
    temp = temp.next
  print()

#------------------------------------------------------------------------------------------------------------------------------

#Task 1: Building Blocks

def check_similar(building_1, building_2):
    c1, c2 = building_1, building_2
    truth = False
    while c1!=None and c2!= None:
        if c1.elem == c2.elem:
            truth = True
            c1, c2 = c1.next, c2.next
        else:
            truth = False
            break
    if c1!=c2:
        truth = False
    if truth == True:
        return "Similar"
    else:
        return "Not Similar"
print('==============Test Case 1=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Similar'
print()

print('==============Test Case 2=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Yellow', 'Green']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Not Similar'
print()

print('==============Test Case 3=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green', 'Blue']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Not Similar'
print()

print('==============Test Case 4=============')
building_1 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green', 'Blue']))
building_2 = createList(np.array(['Red', 'Green', 'Yellow', 'Red', 'Blue', 'Green']))
print('Building 1: ', end = ' ')
printLinkedList(building_1)
print('Building 2: ', end = ' ')
printLinkedList(building_2)
returned_value = check_similar(building_1, building_2)
print(returned_value) #This should print 'Not Similar'
print()

#------------------------------------------------------------------------------------------------------------------------------

#Task 2: Remove Compartment

def remove_compartment(head,n):
    j = 0
    c=head
    while c is not None:
        c = c.next
        j+=1
    c1 = head
    i = 0
    limit = j - n #6 - 2 = 4
    if limit == 0:
        head = c1.next
        return head
    if limit<0:
        return head
    while i<limit-1:
         c1 = c1.next
         i+=1
    c1.next = c1.next.next
    return head
print('==============Test Case 1=============')
head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,2)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 10-->15-->34-->41-->72
print()
print('==============Test Case 2=============')
head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,7)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 10-->15-->34-->41-->56-->72
print()
print('==============Test Case 3=============')
head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,6)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 15-->34-->41-->56-->72
print()

#------------------------------------------------------------------------------------------------------------------------------

#Task 3: Assemble Conga Line

def assemble_conga_line(conga_line):
  c = conga_line
  truth =  True
  while c.next!=None:
    if c.next.elem > c.elem:
        truth = True
        c=c.next
    else:
        truth = False
        break
  return truth


print('==============Test Case 1=============')
conga_line = createList(np.array([10,15,34,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
returned_value = assemble_conga_line(conga_line)
print(returned_value) #This should print True
print()
print('==============Test Case 2=============')
conga_line = createList(np.array([10,15,44,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
returned_value = assemble_conga_line(conga_line)
print(returned_value) #This should print False
print()

#------------------------------------------------------------------------------------------------------------------------------

#Task 4: Word Decoder

def word_Decoder(head):
    c = head
    z = 0
    while c != None:
        c = c.next
        z += 1
    c1 = head
    m = 13%z
    New_head = Node(None,None)
    head3 = New_head
    tail = None
    head3.next = None
    i = 0
    while i<z:
        if i==0 or i%m != 0:
            c1 = c1.next
            i+=1
        elif i!=0 and i%m == 0:

                obj1 = Node(c1.elem)
                obj1.next = tail
                head3.next = obj1
                tail = obj1
                c1 = c1.next
                i+=1
    return New_head


#Driver Code
print('==============Test Case 1=============')
head = createList(np.array(['B', 'M', 'D', 'T', 'N', 'O', 'A', 'P', 'S', 'C']))
print("Encoded Word:")
printLinkedList(head) #This should print B→M→D→T→N→O→A→P→S→C

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)    #This should print None→C→A→T

print('==============Test Case 2=============')

head = createList(np.array(['Z', 'O', 'T', 'N', 'X']))
print("Encoded Word:")
printLinkedList(head) #This should print Z→O→T→N→X

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)    #This should print None→N

#------------------------------------------------------------------------------------------------------------------------------

#Task 5: Alternate Merge

def alternate_merge(head1, head2):
    c1, c2 = head1, head2
    head3 = Node(c1.elem)
    c3 = head3
    c1 = c1.next
    c3.next = c2
    c3 = c2
    c2 = c2.next
    while True:
        if c1 is not None:
            if c2 is not None:
                obj = Node(c1.elem)
                obj2 = Node(c2.elem)
                obj.next = obj2
                c3.next = obj
                c3 = obj2
                c1 = c1.next
                c2 = c2.next
            elif c2 is None:
                obj = Node(c1.elem)
                c3.next = obj
                c1 = c1.next
                obj = c3
                break
        else:
            break
    return head3
print('==============Test Case 1=============')
head1 = createList(np.array([1,2,6,8,11]))
head2 = createList(np.array([5,7,3,9,4]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
printLinkedList(head)    #This should print    1 --> 5 --> 2 --> 7 --> 6 --> 3 --> 8 --> 9 --> 11 --> 4


print('==============Test Case 2=============')
head1 = createList(np.array([5, 3, 2, -4]))
head2 = createList(np.array([-4, -6, 1]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
printLinkedList(head)    #This should print    5 → -4 -> 3 → -6 -> 2 -> 1 -> -4


print('==============Test Case 3=============')
head1 = createList(np.array([4, 2, -2, -4]))
head2 = createList(np.array([8, 6, 5, -3]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)

head = alternate_merge(head1, head2)
print("Merged Linked List:")
printLinkedList(head)    #This should print   4-> 8 → 2-> 6 → -2 → 5 → -4 -> -3

#------------------------------------------------------------------------------------------------------------------------------

#Task 6: Sum of Nodes

def sum_dist(head, arr):
    c1 = head
    sum = 0
    j = 0
    while True:
        if c1.next != None:
            j+=1
            c1 = c1.next
        else:
            j+=1
            break
    c = head
    for i in range(len(arr)):
        k = 0
        if arr[i]>=j:
            sum+=0
        else:
            while True:
                if k!=arr[i]:
                    c = c.next
                    k+=1
                elif k==arr[i]:
                    sum+=c.elem
                    c = head
                    break

    return sum
print('==============Test Case 1=============')
LL1 = createList(np.array([10,16,-5,9,3,4]))
dist = np.array([2,0,5,2,8])
returned_value = sum_dist(LL1, dist)
print(f'Sum of Nodes: {returned_value}') #This should print Sum of Nodes: 4
print()

#------------------------------------------------------------------------------------------------------------------------------

'''Bonus Task: ID Generator'''

def idGenerator(head1, head2, head3):
    c1, c2, c3 = head1, head2, head3
    s = c2.elem+c3.elem
    if s>=10:
      s = s%10
    head4 = Node(s)
    c4 = head4
    c2, c3 = c2.next, c3.next
    while c2 is not None and c3 is not None:
            s = c2.elem+c3.elem
            if s>=10:
                s = s%10
            obj = Node(s)
            c4.next = obj
            c4 = obj
            c2 = c2.next
            c3 = c3.next
    i = 0
    while c1.next is not None:
        i+=1
        c1 = c1.next
    z = 0
    head5 = Node(c1.elem)
    c5 = head5
    c1 = head1
    tail = head4
    c5.next = tail
    #tail.next = head4
    while z<i:
        if c1.next != None:
            obj1 = Node(c1.elem)
            obj1.next = tail
            c5.next = obj1
            tail = obj1
            c1 = c1.next
            z+=1
    return head5
print('==============Test Case 1=============')
head1 = createList(np.array([0,3,2,2]))
head2 = createList(np.array([5,2,2,1]))
head3 = createList(np.array([4,3,2,1]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print  2 → 2 → 3 → 0 → 9 → 5 → 4 → 2


print('==============Test Case 2=============')
head1 = createList(np.array([0,3,9,1]))
head2 = createList(np.array([3,6,5,7]))
head3 = createList(np.array([2,4,3,8]))

print("Linked List 1:")
printLinkedList(head1)
print("Linked List 2:")
printLinkedList(head2)
print("Linked List 3:")
printLinkedList(head3)

result = idGenerator(head1, head2, head3)
print("New ID:")
printLinkedList(result)    #This should print 1 → 9 → 3 → 0 → 5 → 0 → 8 → 5
