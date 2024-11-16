
#Assignment 07

class BTNode:
  def __init__(self, elem):
    self.elem = elem
    self.right = None
    self.left = None

def inorder(root):
  if root == None:
    return

  inorder(root.left)
  print(root.elem, end = ' ')
  inorder(root.right)

def tree_construction(arr, i = 1):
  if i>=len(arr) or arr[i] == None:
    return None
  p = BTNode(arr[i])
  p.left = tree_construction(arr, 2*i)
  p.right = tree_construction(arr, 2*i+1)
  return p


root2 = tree_construction([None, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', None, None, None, 'I', 'J', None, 'k'])
inorder(root2)

Task 1

def convert_mirror(root):
  if root == None: return
  root.left, root.right = root.right, root.left
  convert_mirror(root.left)
  convert_mirror(root.right)
  return root

#DRIVER CODE
root = BTNode(10)
n1 = BTNode(20)
n2 = BTNode(30)
n3 = BTNode(40)
n4 = BTNode(60)

root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root) #Given Tree Inorder Traversal:  40 20 60 10 30
print()

root2 = convert_mirror(root)
print('Mirrored Tree Inorder Traversal: ', end = ' ')
inorder(root2) #Mirrored Tree Inorder Traversal:  30 10 60 20 40

Task 2

def smallest_level(root):
    dic = {}
    level = 0
    def small_value(root, dic, level):
        if root == None: return
        if level not in dic.keys():
            dic[level] = root.elem
        else:
            if root.elem<dic[level]:
                dic[level] = root.elem
        small_value(root.left,dic, level +1 )
        small_value(root.right,dic, level+1 )
    small_value(root, dic, level)
    return dic


#DRIVER CODE
root = tree_construction([None, 4,9,2,3,-5,None,7])
print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root) #Given Tree Inorder Traversal:  3 9 5 4 2 7
print()
print('Level Wise Smallest Value: ', end = ' ')
print(smallest_level(root)) #Level Wise Smallest Value:  {0: 4, 1: 2, 2: -5}

Task 3

def inorder_predecessor(root, x):
    def predecessor(root):
        if root.right == None: return root
        return predecessor(root.right)
    if root == None: return
    if x.elem > root.elem:
        inorder_predecessor(root.right, x)
    if x.elem < root.elem:
        inorder_predecessor(root.left, x)
    if root.elem == x.elem:
        if root.left != None:
            return predecessor(root.left)
        else:
            return root





#DRIVER CODE
root = BTNode(20)
n1 = BTNode(8)
n2 = BTNode(22)
n3 = BTNode(4)
n4 = BTNode(12)
n5 = BTNode(10)
n6 = BTNode(14)

root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

n4.left = n5
n4.right = n6

print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root) #Given Tree Inorder Traversal:  4 8 10 12 14 20 22
print()

x = root
print(f'Inorder predecessor of node {x.elem}: {inorder_predecessor(root, x).elem}') #Inorder predecessor of node 20: 14

Task 4

def LCA(root, x, y):
    if root == None: return
    elif root.elem == x.elem  or root.elem == y.elem :
        return  root.elem
    elif x.elem<root.elem<y.elem or x.elem>root.elem>y.elem :
        return root.elem
    elif x.elem<root.elem and y.elem<root.elem:
        return LCA(root.left, x, y)
    elif x.elem>root.elem and y.elem>root.elem:
        return LCA(root.right, x, y)
#DRIVER CODE
#Write by yourself from the given tree
#check all the sample inputs given
root = BTNode(15)
n1 = BTNode(10)
n2 = BTNode(25)
n3 = BTNode(8)
n4 = BTNode(12)
n5 = BTNode(20)
n6 = BTNode(30)
n7 = BTNode(6)
n8 = BTNode(9)
n9 = BTNode(18)
n10 = BTNode(22)
root.left, root.right = n1, n2
n1.left, n1.right = n3, n4
n3.left, n3.right = n7, n8
n2.left, n2.right = n5, n6
n5.right, n5.left = n9, n10
print(f"LCA({n7.elem},{n4.elem}) = {LCA(root, n7, n4)}")
print(f"LCA({n5.elem},{n7.elem}) = {LCA(root, n5, n7)}")
print(f"LCA({n9.elem},{n10.elem}) = {LCA(root, n9, n10)}")
print(f"LCA({n5.elem},{n2.elem}) = {LCA(root, n5, n2)}")
print(f"LCA({n1.elem},{n4.elem}) = {LCA(root, n1, n4)}")

Task 5

import numpy as np
def sumTree(root):
    sum = np.array([0])
    def adder(root, level, sum):
        if root == None: return
        if level != 0:

            sum[0] += root.elem%level

        else:

            sum[0] += root.elem

        left = adder(root.left, level+1, sum)
        right = adder(root.right, level+1, sum)
    adder(root, 0, sum)
    return sum[0]
#Driver Code
#Input 1
root1 = BTNode(9)
node2 = BTNode(4)
node3 = BTNode(5)
node4 = BTNode(18)
node5 = BTNode(14)
node6 = BTNode(3)
node7 = BTNode(54)
node8 = BTNode(12)
node9 = BTNode(8)
node10 = BTNode(91)
node11 = BTNode(56)

root1.left = node2
root1.right = node3

node2.left = node4

node3.left = node5
node3.right = node6

node4.left = node7
node4.right = node8

node5.left = node9

node8.left = node10
node8.right = node11

print(sumTree(root1)) #This should print 15

Task 6

def swap_child(root, level, M):
    if root == None: return
    if level == M: return
    root.right, root.left = root.left, root.right
    swap_child(root.left, level+1, M)
    swap_child(root.right, level+1, M)
    return root
#Driver Code
root=BTNode('A')
n1 = BTNode("B")
n2 = BTNode("C")
n3 = BTNode("D")
n4 = BTNode("E")
n5 = BTNode("F")
n6 = BTNode("G")
n7 = BTNode("H")
n8 = BTNode("I")
n9 = BTNode("J")
root.right, root.left = n2, n1
n1.left, n1.right = n3, n4
n2.right = n5
n3.left, n3.right = n6, n7
n4.left = n8
n5.left = n9

print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root)   #Given Tree Inorder Traversal: G D H B I E A C J F
print()

root2 = swap_child(root, 0, 2)
print('Swapped Tree Inorder Traversal: ', end = ' ')
inorder(root2)  #Swapped Tree Inorder Traversal: J F C A I E B G D H


Task 7

def subtract_summation(root):
    def adder(root):
        if root == None: return 0
        left = adder(root.left)
        right = adder(root.right)
        return left + right + root.elem
    sum = adder(root.left) - adder(root.right)
    return sum
#Driver Code
root=BTNode(71)
n1 = BTNode(27)
n2 = BTNode(62)
n3 = BTNode(80)
n4 = BTNode(75)
n5 = BTNode(87)
n6 = BTNode(56)
n7 = BTNode(41)
n8 = BTNode(3)
n9 = BTNode( 19 )
n10 = BTNode(89)
root.left, root.right = n1, n2
n1.left, n1.right = n3, n4
n3.left, n3.right = n5, n6
n2.left, n2.right = n7,  n8
n8.left, n8.right = n9, n10
print(subtract_summation(root)) #This should print 111

Bonus Task

def level_sum(root):
    def adder(root, level, odd):
        if root == None: return 0
        left = adder(root.left , level+1, odd)
        right = adder(root.right , level+1, odd )
        if odd == True:
            if level%2 != 0: return left+right+root.elem

        elif odd == False:
            if level%2 == 0: return left+right+root.elem
        return  left+right
    sum = adder(root, 0, True) - adder(root, 0, False)
    return sum
#DRIVER CODE
root = BTNode(1)
n2 = BTNode(2)
n3 = BTNode(3)
n4 = BTNode(4)
n5 = BTNode(5)
n6 = BTNode(6)
n7 = BTNode(7)
n8 = BTNode(8)
root.left = n2
root.right = n3

n2.left = n4
n3.left = n5
n3.right = n6

n5.left = n7
n5.right = n8


print(level_sum(root)) #This should print 4
