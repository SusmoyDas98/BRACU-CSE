#Assignment 01
#Assignment Part-2

import numpy as np

#Task 01: Merge Lineup
def mergeLineup(pokemon_1, pokemon_2):
        arr1 = np.zeros(len(pokemon_1), dtype=int)
        J = len(pokemon_1)-1
        for i in range(0,len(pokemon_1)):
            a = pokemon_1[i]
            b = pokemon_2[J]
            if a == None :
                a = 0
            if b == None:
                b = 0
            arr1[i] = a+b
            J-=1
        return arr1


print("///  Task 01: Merge Lineup  ///")
pokemon_1 = np.array([12, 3, 25, 1, None])
pokemon_2 = np.array([5, -9, 3, None, None] )
returned_value =mergeLineup(pokemon_1, pokemon_2)
print(f'Task 1: {returned_value}') # This should print [12, 3, 28, -8, 5]


pokemon_1 = np.array([4, 5, -1, None, None])
pokemon_2 = np.array([2, 27, 7, 12, None])
returned_value =mergeLineup(pokemon_1, pokemon_2)
print(f'Task 1: {returned_value}') # This should print [4,17,6,27,2]

#------------------------------------------------------------------------------------------------------------------------------

# Task 02: Discard Cards
def leftshift(array, indx):
    for i in range(indx, len(array)-1):
        array[i] = array[i+1]
    array[len(array)-1] = 0
    return array
def discardCards(cards, t):
    c = 0
    i = 0
    while i<len(cards):
        if cards[i] == t:
            c+=1
            if c%2 != 0:
                cards = leftshift(cards, i)
                i-=1
        i+=1
    return cards
print("///  Task 02: Discard Cards  ///")
cards = np.array([1,3,7,2,5,2,2,2,0])
returned_value = discardCards(cards, 2)
print(f'Task 2: {returned_value}') # This should print [1,3,7,5,2,2,0,0,0]

cards = np.array([5,5,5,0,0])
returned_value = discardCards(cards, 5)
print(f'Task 2: {returned_value}') # This should print [5,0,0,0,0]

#------------------------------------------------------------------------------------------------------------------------------

# Task 03: DUBER Fare Splitting
def findGroups(money, fare):
    arr = np.array([False]*len(money))
    group = 1
    for i in range(len(money)):
      if money[i]<fare:
          if arr[i] == False:
              x = fare - money[i]
              for j in range(i+1, len(money)):
                  if money[j] == x:
                      if arr[j] == False:
                          print(f"Group{group} : {money[i]},{money[j]}")
                          arr[i], arr[j] = True, True
                          group +=1
                          x = 0

      else:
          if arr[i] == False:
              print(f"Group{group} : {money[i]}")
              group += 1
              arr[i] = True
    if False in arr:
        print("Ungrouped: ", end = "")
        for i in range(len(arr)):
            if arr[i] == False:
                print(money[i],end=" ")

print("///  Task 03: DUBER Fare Splitting  ///")
money = np.array( [120, 100, 150, 50, 30])
fare = 150
print(f'Task 3:')
findGroups(money, fare) # This should print

# Group 1 : 120, 30
# Group 2 : 100, 50
# Group 3 : 150


money = np.array( [60, 150, 60, 30, 120, 30])
fare = 180
print(f'Task 3:')
findGroups(money, fare) # This should print

# Group 1 : 60, 120
# Group 2 : 30, 150
# Ungrouped : 30 60

#------------------------------------------------------------------------------------------------------------------------------

# Task 04: Get Those Hobbies
def analyzeHobbies(*participants): #(* arguments) is used for variable number of parameters
    # TO DO
    # Print outputs inside the method
    x = 0
    for i in range(len(participants)):
         x+=len(participants[i])
    arr2 = np.array([None]*x)
    idx  =  0
    for i in participants:
        for j in range(len(i)):
            if i[j] not in arr2:
                    arr2[idx] = i[j]
                    idx += 1
    n = 0
    for k in range(len(arr2)):
        if arr2[k] != None:
            n+=1

    arr3 = np.array([None]*n)
    for l in range(len(arr2)):
        if arr2[l] != None:
            arr3[l] = arr2[l]
    print(f"Unique Activities in town:\n{arr3}")
    for m in range(len(arr3)):
        c = 0
        for n in range(len(participants)):
            for o in range(len(participants[n])):
                if participants[n][o] == arr3[m]:
                    c+=1
        print(f"{c} particiants likes {arr3[m]}")




print("///  Task 04: Get Those Hobbies  ///")
participant_1 = np.array( ["Hiking", "Reading", "Photography", "Cooking"])
participant_2 = np.array( ["Reading", "Hiking", "Painting"])
participant_3 = np.array( ["Hiking", "Cooking", "Photography"])
print(f'Task 4:')
analyzeHobbies(participant_1, participant_2, participant_3) #This should print

#Unique Activities in the Town:
#['Photography', 'Painting', 'Cooking', 'Reading', 'Hiking']

#Statistics:
#2 participant(s) like(s) Photography.
#1 participant(s) like(s) Painting.
#2 participant(s) like(s) Cooking.
#2 participant(s) like(s) Reading.
#3 participant(s) like(s) Hiking.



participant_1 = np.array( ["Gardening", "Traveling"])
participant_2 = np.array( ["Singing", "Gardening", "Painting"])
print(f'Task 4:')
analyzeHobbies(participant_1, participant_2) #This should print

#Unique Activities in the Town:
#[Gardening, Traveling, Singing, Painting]

#Statistics:
#2 participant(s) like(s) Gardening.
#1 participant(s) like(s) Traveling.
#1 participant(s) like(s) Singing.
#1 participant(s) like(s) Painting.

#------------------------------------------------------------------------------------------------------------------------------

# Bonus Ungraded Task: Look and Say
def look_and_say(arr):
  arr2 = np.zeros(100,dtype = int)
  idx = 0
  i = 0
  while i < len(arr):
    c = 1
    j = i+1
    while j < len(arr):
        if  arr[j] == arr[i]:
            c+=1
            j+=1
        else:

            break
    arr2[idx] = c
    arr2[idx+1] = arr[i]
    idx+=2
    i = j
  return arr2

print("///  Bonus Task: Look and Say  ///")
arr = np.array([1,3,1,1,2,2,2,1])
returned_value = look_and_say(arr)
print(f'Bonus Task: {returned_value}') # This should print [1,1,1,3,2,1,3,2,1,1]
#Hint: The size of the new array will never be more than 100.
#[You need not worry about the extra zeroes at the end of your resulting array]

#------------------------------------------------------------------------------------------------------------------------------

'''For Assignment Part-1, you can create new code cells in the below and write your codes there. Also you should write driver codes to test your code for part-1.'''

#Assignment Part-1
#Write 3 methods and driver codes for this part.

def mean(array):
    x = 0
    for i in range(len(array)):
        x+=array[i]
    m = str(x/len(array))
    index = 0
    for i in range(len(m)):
        if m[i] == ".":
            index = i
    return float(m[0:index+11:])
def standarddeviation(array):
    a = 0
    m  = mean(array)
    for i in range(len(array)):
        a += (array[i]-m)**2
    std = str((a/(len(array)-1))**(0.5))

    index = 0
    for i in range(len(std)):
        if std[i] == ".":
            index = i
    return float(std[0:index+3:])
def newArray(array, diff):
    m = standarddeviation(array)
    n = mean(array)
    arr = np.array([0]*len(array),dtype = int)
    j = 0
    c = 0
    for i in range(len(array)):
        Z = (array[i] - n)/(m)
        if abs(Z) >= float(diff):
            arr[j] = array[i]
            c+=1
        j+=1
    arr2 = np.array([0]*c,dtype = int)
    x = 0
    for k in range(len(arr)):
        if arr[k] != 0:
            arr2[x] =  arr[k]
            x+=1

    return arr2


arr = [10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4]
print(f"The mean of the numbers is: {mean(arr)}")
print(f"The standard deviation is: {standarddeviation(arr)}")
print(f"New array: {newArray(arr, 1.5)}")
