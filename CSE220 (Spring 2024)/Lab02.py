#Assignment 02

import numpy as np

#You must run this cell to print matrix and for the driver code to work
def print_matrix(m):
  row,col = m.shape
  for i in range(row):
    c = 1
    print('|', end='')
    for j in range(col):
      c += 1
      if(len(str(m[i][j])) == 1):
        print(' ',m[i][j], end = '  |')
        c += 6
      else:
        print(' ',m[i][j], end = ' |')
        c += 6
    print()
    print('-'*(c-col))

#------------------------------------------------------------------------------------------------------------------------------

#Task 1: Zigzag Walk

def walk_zigzag(floor):
   
  row, col = floor.shape[0], floor.shape[1]
  idx = 0
  for i in range(col):
    if i%2 == 0:
        for j in range(0,row, 2):
            if j==row-1:
                idx = row-2
            if j==row-2:
                idx = row-1
            if j<row:
                print(floor[j][i],end=' ')
        print()

    elif i%2 != 0:
        for j in range(idx, -1, -2):
            if j>-1:
                print(floor[j][i],end=" ")
        print()
floor = np.array([[ '3' , '8' , '4' , '6' , '1'],
                  ['7' , '2' , '1' , '9' , '3'],
                  ['9' , '0' , '7' , '5' , '8'],
                  ['2' , '1' , '3' , '4' , '0'],
                  ['1' , '4' , '2' , '8' , '6']]
                )

print_matrix(floor)
print('Walking Sequence:')
walk_zigzag(floor)
#This should print
# 3 9 1
# 1 2
# 4 7 2
# 4 9
# 1 8 6
print('################')
floor = np.array([[ '3' , '8' , '4' , '6' , '1'],
                  ['7' , '2' , '1' , '9' , '3'],
                  ['9' , '0' , '7' , '5' , '8'],
                  ['2' , '1' , '3' , '4' , '0']]
                )

print_matrix(floor)
print('Walking Sequence:')
walk_zigzag(floor)
#This should print
# 3 9
# 1 2
# 4 7
# 4 9
# 1 8

#------------------------------------------------------------------------------------------------------------------------------

#Task 2: Row Rotation Policy of BRACU Classroom

def row_rotation(exam_week, seat_status):
     
    row, col = seat_status.shape[0],seat_status.shape[1]
    idx = 0
    arr1 = np.array([None]*col,dtype = str)
    for j in range(1,exam_week,1):
        for l in range(col):
            arr1[l] = seat_status[row-1][l]
        for k in range(row-1, -1,-1):
            seat_status[k] = seat_status[k-1]
        seat_status[0] = arr1
    for i in range(row):
        if "AA" in seat_status[i]:
          idx =  i
          break
    print_matrix(seat_status)
    return idx+1


seat_status = np.array([[ 'A' , 'B' , 'C' , 'D' , 'E'],
                  ['F' , 'G' , 'H' , 'I' , 'J'],
                  ['K' , 'L' , 'M' , 'N' , 'O'],
                  ['P' , 'Q' , 'R' , 'S' , 'T'],
                  ['U' , 'V' , 'W' , 'X' , 'Y'],
                  ['Z' , 'AA' , 'BB' , 'CC' , 'DD']])
exam_week=3
print_matrix(seat_status)
print()
row_number=row_rotation(exam_week, seat_status) #This should print modified seat status after rotation
print(f'Your friend AA will be on row {row_number}') #This should print Your friend AA will be on row 2

#------------------------------------------------------------------------------------------------------------------------------

#Task 3: Matrix Manipulation

def reverse_Matrix(matrix):
     
    row, col = len(matrix), len(matrix[0])
    arr1 = np.array([[None]*col]*row)
    idx = 0
    for i in range(row-1,-1,-1):
        for j in  range(col-1,-1,-1):
            arr1[idx][col-1-j] = matrix[i][j]
        idx += 1
    return arr1


matrix = np.array([
[14,  8,  0,  4],
[9,  8,  13,  13],
[9,  3,  1,  4],
[2,  10,  13,  6]
])
print_matrix(matrix)
reversed_matrix = reverse_Matrix(matrix)
print_matrix(reversed_matrix)

#This should print
#|  6  |  13 |  10 |  2  |
#-------------------------
#|  4  |  1  |  3  |  9  |
#-------------------------
#|  13  |  13  |  8 |  9 |
#-------------------------
#|  4 |  0  |  8  |  14  |
#-------------------------

#------------------------------------------------------------------------------------------------------------------------------

#Task 4: Chess Piece

def show_knight_move(knight):
   
  arr = np.array([[0]*8]*8)
  row1, col1 = len(arr), len(arr[0])
  rowpos, colpos = knight[0], knight[1]
  position  = np.array([[-2,1],[-2,-1],[2, 1],[2, -1],[-1,-2],[1, -2],[-1,2],[1,2]])
  arr[rowpos][colpos] =  rowpos*22
  for i in range(len(position)):
    a, b = rowpos+position[i][0], colpos+position[i][1]
    if a<0 or b<0 or b>col1 or a>row1:
        pass
    else:
        arr[a][b] = 3
  return arr

knight = (3,4)
chess_board = show_knight_move(knight)
print_matrix(chess_board)
#This Should print
#| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
#------------------------------------------
#| 0 | 0 | 0 | 3 | 0 | 3 | 0 | 0 |
#------------------------------------------
#| 0 | 0 | 3 | 0 | 0 | 0 | 3 | 0 |
#------------------------------------------
#| 0 | 0 | 0 | 0 | 66 | 0 | 0 | 0 |
#------------------------------------------
#| 0 | 0 | 3 | 0 | 0 | 0 | 3 | 0 |
#------------------------------------------
#| 0 | 0 | 0 | 3 | 0 | 3 | 0 | 0 |
#------------------------------------------
#| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
#------------------------------------------
#| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
#-----------------------------------------

#------------------------------------------------------------------------------------------------------------------------------

#Task 5: Matrix Compression

def compress_matrix(mat):
    row,col = len(mat), len(mat[1])
    arr = np.zeros((row//2,col//2),dtype = int)
    idx = 0

    for i in range(0,row,2):
        c = 0
        sum = 0
        for j in range(0,col,2):
            sum +=  mat[i][j]
            sum +=  mat[i][j+1]
            sum += mat[i+1][j]
            sum += mat[i+1][j+1]
            arr[idx][c] = sum
            sum = 0
            c+=1
        idx+=1
    return arr

matrix=np.array([[1,2,3,4],
                 [5,6,7,8],
                 [1,3,5,2],
                 [-2,0,6,-3]
                 ])
print_matrix(matrix)
returned_array=compress_matrix(matrix)
print_matrix(returned_array)
#This should print
#|  14  |  22 |
#--------------
#|  2  |  10  |
#--------------

#------------------------------------------------------------------------------------------------------------------------------

#Task 6: Game Arena

def play_game(arena):
    row, col = len(arena), len(arena[0])
    sum = 0
    for i in range(row):
      for j in range(col):
          if arena[i][j]%50 == 0 and arena[i][j] !=0:
              if i ==0 :
                  if j == 0:
                      if arena[i][j+1] == 2:
                          sum += 2
                      if arena[i+1][j]==2:
                          sum += 2
                  elif j==col-1:
                      if arena[i][j-1] == 2:
                          sum += 2
                      if arena[i+1][j]==2:
                          sum += 2
                  else:
                      if arena[i][j+1] == 2:
                          sum += 2
                      if arena[i+1][j]==2:
                          sum += 2
                      if arena[i][j-1] == 2:
                          sum += 2
              elif  i==row-1:
                  if j == 0:
                      if arena[i][j+1] == 2:
                          sum += 2
                      if arena[i-1][j]==2:
                          sum += 2
                  elif j==col-1:
                      if arena[i][j-1] == 2:
                          sum += 2
                      if arena[i-1][j]==2:
                          sum += 2
                  else:
                      if arena[i][j+1] == 2:
                          sum += 2
                      if arena[i-1][j]==2:
                          sum += 2
                      if arena[i][j-1] == 2:
                          sum += 2
              else:
                  if j == 0:
                      if arena[i][j+1] == 2:
                          sum += 2
                      if arena[i+1][j]==2:
                          sum += 2
                      if arena[i-1][j]==2:
                          sum += 2
                  elif j==col-1:
                      if arena[i][j-1] == 2:
                          sum += 2
                      if arena[i+1][j]==2:
                          sum += 2
                      if arena[i-1][j]==2:
                          sum += 2
                  else:
                      if arena[i][j+1] == 2:
                          sum += 2
                      if arena[i+1][j]==2:
                          sum += 2
                      if arena[i][j-1] == 2:
                          sum += 2
                      if arena[i-1][j]==2:
                          sum += 2
    if sum>=10:
        print(f"Points Gained: {sum}. Your team has survived the game.")
    else:
        print(f"Points Gained: {sum}. Your team is out.")


arena=np.array([[0,2,2,0],
                [50,1,2,0],
                [2,2,2,0],
                [1,100,2,0]
                ])
print_matrix(arena)
play_game(arena)
#This should print
#Points Gained: 6. Your team is out.

print(".....................")
arena=np.array([[0,2,2,0,2],
                [1,50,2,1,100],
                [2,2,2,0,2],
                [0,200,2,0,0]
                ])
print_matrix(arena)
play_game(arena)
#This should print
#Points Gained: 14. Your team has survived the game.


#------------------------------------------------------------------------------------------------------------------------------


#Bonus Task: Primary vs Secondary Diagonal

def check_diagonal(matrix1, matrix2):
  row1, col1 = matrix1.shape[0], matrix1.shape[1]
  row2, row2 = matrix2.shape[0], matrix2.shape[1]
  arr1 = np.zeros(row1 , dtype =  int)
  truth = False
  col = col1-1
#  arr2 = np.zeros(row2 , dtype =  int)
  for i in range(row1):
    if matrix1[i][col] == matrix2[col][col]:
        truth = True
        col-=1
    else:
        truth = False
        break
  if truth == True:
    print("Yes")
  else:
    print("No")

array1 = np.array([[0, 4, 1], [7, 2, 5], [3, 6, 0]])
array2 = np.array([[3, 6, 0], [5, 2, 7], [0, 4, 1]])

check_diagonal(array1, array2) #This should print YES
print(".............")
array1 = np.array([[0, 9, 9, 1], [9, 0, 2, 9], [9, 3, 0, 9], [4, 9, 9, 0]])
array2 = np.array([[4, 9, 9, 0], [9, 0, 3, 9], [9, 0, 2, 9], [0, 9, 5, 1]])

check_diagonal (array1, array2) #This should print NO
