#Assignment 06

import numpy as np

#Task 1
class vehicleNodes:
  def __init__(self, brand, vehicle_type, rent, passenger, next = None):
    self.brand=brand
    self.vehicle_type = vehicle_type
    self.rent = rent
    self.passenger = passenger
    self.next = next


class VehicleHashTable:
  def __init__(self, size):
    self.vehicleTable = [None]*size
    self.empty_slot = {}
    for i in range(size):
      self.empty_slot[i] = False

  def create_from_vehicle_info_array(self, arr):
    for i in arr:
      self.insert_vehicle(i)

  def print_vehicle_hashtable(self):
    idx = 0
    for i in self.vehicleTable:
      print(idx, ':', end = ' ')
      head = i
      while head != None:
        print(f'(Brand: {head.brand}, Type: {head.vehicle_type}, Rent: {head.rent}, No. of Passengers: {head.passenger})', end = '---->')
        head = head.next
      print('None')
      print()
      idx += 1

  def find_empty_slot(self):
    for k,v in self.empty_slot.items():
      idx = k
      del self.empty_slot[k]
      return idx



  def __hash_function(self, brand):
        sum = 0
        def functionmaker(brand,sum):
              if brand=='' : return sum
              sum += ord(brand[0])
              return functionmaker(brand[1::],sum)
        index = functionmaker(brand, 0)%len(self.vehicleTable)
        
        if index in self.empty_slot:
          del self.empty_slot[index]
        return index
  def insert_vehicle(self, vehicle):
        a = vehicleNodes(vehicle[0],vehicle[1],vehicle[2],vehicle[3],None)
        indx = self.__hash_function(vehicle[0])
        if self.vehicleTable[indx] is None:
            self.vehicleTable[indx] = a
        elif self.vehicleTable[indx] is not None:
            if vehicle[0] == self.vehicleTable[indx].brand:
                a.next = self.vehicleTable[indx]
                self.vehicleTable[indx] = a
            else:
                b = self.find_empty_slot()
                self.vehicleTable[b] = a
        return self.vehicleTable

#DRIVER CODE
vehicle_info = [('Toyota', 'Private Car', 500, 4), ('Jeep', 'SUV', 950, 6), ('Lamborghini', 'SUV', 6900, 6), ('Hyundai', 'Bike', 100, 1), ('BMW', 'Private Car', 1000, 8), ('Honda', 'Bike', 150, 1), ('Ferrari', 'Private Car', 2500, 4), ('BMW', 'Minivan', 5800, 7)]

vt = VehicleHashTable(len(vehicle_info))

vt.create_from_vehicle_info_array(vehicle_info)
print("============== Printing The HashTable ==============")
vt.print_vehicle_hashtable()

# should print
# 0 : (Brand: Toyota, Type: Private Car, Rent: 500, No. of Passengers: 4)---->None

# 1 : (Brand: Lamborghini, Type: SUV, Rent: 6900, No. of Passengers: 6)---->None

# 2 : (Brand: Hyundai, Type: Bike, Rent: 100, No. of Passengers: 1)---->None

# 3 : (Brand: Honda, Type: Bike, Rent: 150, No. of Passengers: 1)---->None

# 4 : (Brand: Jeep, Type: SUV, Rent: 950, No. of Passengers: 6)---->None

# 5 : (Brand: Ferrari, Type: Private Car, Rent: 2500, No. of Passengers: 4)---->None

# 6 : (Brand: BMW, Type: Minivan, Rent: 5800, No. of Passengers: 7)---->(Brand: BMW, Type: Private Car, Rent: 1000, No. of Passengers: 8)---->None

# 7 : None


#------------------------------------------------------------------------------------------------------------------------------


#Task 2

#Complete the following methods:

__hash_function()

search_hashtable()

class Node_pair:
  def __init__(self, key, value, next = None):
    self.key, self.value, self.next = key, value, next


class Hashtable:
  def __init__(self, size):
    self.ht = [None]*size


  def insert(self, s):
    if self.search_hashtable(s) == 'Found':
      print(s,'Already Inserted. Cannot reinsert.')
      print('===============================')
      return
    hashed_index = self.__hash_function(s[0])
    pair = Node_pair(s[0], s[1])
    if self.ht[hashed_index] == None:
      self.ht[hashed_index] = pair
    else:
      pair.next = self.ht[hashed_index]
      self.ht[hashed_index] = pair


  def create_from_array(self, arr):
    for i in arr:
      self.insert(i)

  def print_hashtable(self):
    idx = 0
    for i in self.ht:
      print(idx, ':', end = ' ')
      head = i
      while head != None:
        print(f'(key: {head.key}, value: {head.value})', end = '-->')
        head = head.next
      print('None')
      print()
      idx += 1

  def __hash_function(self, key):
    def functionmaker(strg, indx, sum=""):
        if indx>=len(strg) : return sum
        sum += str(ord(strg[indx]))+str(ord(strg[indx+1]))
        return functionmaker(strg, indx+2, sum)
    if len(key)%2==0: return int(functionmaker(key, 0)) % len(self.ht)
    else: return int(functionmaker(key+"N", 0)) % len(self.ht)
  def search_hashtable(self, s):
    indx = self.__hash_function(s[0])
    if self.ht[indx] == None: return "Not Found"
    else:
        a  =  self.ht[indx]
        def finder(head):
            if head == None: return "Not Found"
            if head.key == s[0] : return "Found"
            return finder(head.next)
        return finder(a)




#Driver Code
arr = [('Colt', 360), ('Cordelius', 730), ('Shelly', 300), ('Doug', 1200), ('Emz', 520), ('Bo', 580)]
ht = Hashtable(5)
ht.create_from_array(arr)
ht.print_hashtable()

print('======================')
result = ht.search_hashtable(('Doug', 1200))

print(f'(Doug, 1200) {result}')

print('======================')
ht.insert(('Doug', 1200))
ht.print_hashtable()

print('======================')
result = ht.search_hashtable(('Edgar', 320))

print(f'(Edgar, 320) {result}')

print('======================')
ht.insert(('Edgar', 320))
ht.print_hashtable()

print('======================')
result = ht.search_hashtable(('Edgar', 320))

print(f'(Edgar, 320) {result}')

#------------------------------------------------------------------------------------------------------------------------------

#Task 3

Implement the __hash_function() and insert() methods

class Node:
  def __init__(self, value=None, next = None):
    self.value = value
    self.next = next

class HashTable:
  def __init__(self, length):
    n = Node()
    self.ht = [n] * length
    self.length = length

  def show(self):
    count = 0
    for i in self.ht:
      temp = i
      print(count, end=" ")
      while temp!=None:
        print (temp.value, end="-->")
        temp = temp.next
      count += 1
      print()
  def __hash_function(self, key):
    def functionmaker(word, indx, sum):
        if indx>=len(word): return sum
        sum += ord(word[indx])
        return functionmaker(word, indx+2, sum)
    if len(key)%2 == 0 : return functionmaker(key, 0, 0) % len(self.ht)
    elif len(key)%2 != 0: return functionmaker(key, 1, 0) % len(self.ht)

  
  def insert(self, key, value):
    a = Node((key,value), None)
    def finder(head, val, node):
            if  head.next == None : return
            if head.value[1] > val> head.next.value[1]:
                node.next = head.next
                head.next =  node
                return
            return finder(head.next, val, node)
    indx = self.__hash_function(key)
    if self.ht[indx].value == None:
        self.ht[indx] =  a
    else:
        c1 = self.ht[indx]
        if c1.next == None:
            if c1.value[1] > value:
                c1.next = a
            elif c1.value[1]<value:
                a.next = c1
                c1 = a
            return
        return finder(c1, value, a)


#Driver Code
ht = HashTable(3)


ht.insert("apple", 20)
ht.insert("coconut", 90)
ht.insert("cherry", 50)
ht.show()
print("------------")
ht.insert("banana", 30)
ht.insert("pineapple", 50)
ht.show()

# Driver Code Output:
# 0 ('coconut', 90)-->
# 1 ('apple', 20)-->
# 2 ('cherry', 50)-->
# ------------
# 0 ('coconut', 90)-->('pineapple', 50)-->('banana', 30)-->
# 1 ('apple', 20)-->
# 2 ('cherry', 50)-->

#------------------------------------------------------------------------------------------------------------------------------

#Task 4

'''Implement the __hash_function() and remove() methods'''

class Node_pair:
  def __init__(self, key, value, next = None):
    self.key, self.value, self.next = key, value, next


class Hashtable:
  def __init__(self, size):
    self.ht = [None]*size


  def insert(self, s):
    hashed_index = self.__hash_function(s[0])
    pair = Node_pair(s[0], s[1])
    if self.ht[hashed_index] == None:
      self.ht[hashed_index] = pair
    else:
      pair.next = self.ht[hashed_index]
      self.ht[hashed_index] = pair


  def create_from_array(self, arr):
    for i in arr:
      self.insert(i)

  def print_hashtable(self):
    idx = 0
    for i in self.ht:
      print(idx, ':', end = ' ')
      head = i
      while head != None:
        print(f'({head.key}, {head.value})', end = '-->')
        head = head.next
      print('None')
      idx += 1


   
  def __hash_function(self, key):
    return (key+3)%6



   
  def remove(self, key):
    indx = self.__hash_function(key)
    def finder(head, key)    :
        if head.next == None : return
        if head.next.key == key:
            head.next =  head.next.next
            return
        return finder(head.next, key)
    c1 = self.ht[indx]
    if  self.ht[indx].key == key:
        self.ht[indx] = self.ht[indx].next
        return
    return finder(c1, key)


#Driver Code
arr=[(34, 'Abid') , (4, 'Rafi'), (6, 'Karim'), (3, 'Chitra'), (22, 'Nilu')]
ht = Hashtable(6)
ht.create_from_array(arr)
ht.print_hashtable()
#This should print

#0: (3, “Chitra”) --> None
#1: (22, “Nilu”) --> (4, “Rafi”) --> (34, “Abid”) --> None
#2: None
#3: (6, “Karim”) --> None
#4: None
#5: None

print('======================')

ht.remove(9)
ht.print_hashtable()
#This should print

#0: (3, “Chitra”) --> None
#1: (22, “Nilu”) --> (4, “Rafi”) --> (34, “Abid”) --> None
#2: None
#3: (6, “Karim”) --> None
#4: None
#5: None

print('======================')
print('======================')

ht.remove(4)
ht.print_hashtable()
#This should print

#0: (3, “Chitra”) --> None
#1: (22, “Nilu”) --> (34, “Abid”) --> None
#2: None
#3: (6, “Karim”) --> None
#4: None
#5: None
