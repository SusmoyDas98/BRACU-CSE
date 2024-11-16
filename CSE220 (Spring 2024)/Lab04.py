#Assignment 4
import numpy as np

#Assignment Part 1
class Patient:
  def __init__(self, id, name, age, bloodgroup,prev = None,next=None):
        self.id = id
        self.name = name
        self.bloodgroup = bloodgroup
        self.prev = prev
        self.next = next
        self.age = age

class WRM:
  def __init__(self):
    self.dh = Patient(None, None, None, None)
    self.c1 = self.dh
    self.c1.next = self.dh
    self.c1.prev = self.dh
  def registerPatient(self,id, name, age, bloodgroup):
    p1 = Patient(id, name, age, bloodgroup)
    p1.next = self.dh
    p1.prev = self.c1
    self.c1.next = p1
    self.dh.prev = p1
    self.c1 = p1
    print("-------------------------------------------")
    print(f"Successfully registered A New Patient.")
    print("-------------------------------------------")
  def servePatient(self):
    print(".............................................\n")
    if self.dh.next == self.dh:
        print("NO PATIENTS IN THE WAITING ROOM")
        print("..........................................")
        return

    c2 = self.dh.next
    c2.prev.next = c2.next
    c2.next.prev = c2.prev
    print("____________________________________________\n")
    print(" Successfully served a patient ")
    print("____________________________________________")
  def showAllPatient(self):
    print(".............................................\n")
    if self.dh.next == self.dh:
        print("NO PATIENTS IN THE WAITING ROOM")
        print("..........................................")
        return
    print("All patients:\n")
    c2 = self.dh.next
    while c2.name is not None:
        print("Name:",c2.name,"Id:", c2.id, "Age:", c2.age, "Bloodgroup:", c2.bloodgroup,"\n")
        c2 = c2.next
    print(".............................................")
  def canDoctorGoHome(self):
    print("____________________________________________\n")
    if self.dh.next == self.dh:

        print("Yes, the doctor can now go home.")
    else:
        print("No, there are more patietns in the Waiting Room.")
    print("____________________________________________")
  def cancelAll(self):

    self.dh.next = self.dh
    self.dh.prev = self.dh
    self.empty = True
    print("____________________________________________\n")
    print("All appointments are cancelled")
    print("____________________________________________")

  def ReverseTheLine(self):
    print("..........................................")
    if self.dh.next == self.dh:
        print("NO PATIENTS IN THE WAITING ROOM")
        print("..........................................")
        return
    c2 = self.dh
    while c2.next != self.dh:
        c2.next, c2.prev, c2 = c2.prev, c2.next, c2.next
    c2.next , c2.prev = c2.prev, c2.next
    self.c1 = c2
    print("The line of patients has been reversed.")
    print("..........................................")

print("**Welcome to Waiting Room Management System**")

patient = WRM()
print("-------------------------------------------")
print(f"Choose an option:\n(1) Register a new patient\n(2) Serve a patient\n(3) Cancel all appointments\n(4) Can Doctor Go Home?\n(5) Show all patients\n(6) Reverse the line of patients\n(7) EXIT")
print("-------------------------------------------")
while True:
    option = int(input("Enter your option: "))
    if option<=0 or option>7:
        print("Option not available")
    else:
        if option==1:
            patient.registerPatient(id=int(input("ID: ")), name=input("Patient's Name: "), age=int(input("Age: ")), bloodgroup=input("Blood Group: "))
        elif option == 2:
            patient.servePatient()
        elif option == 3:
            patient.cancelAll()
        elif option == 4:
            patient.canDoctorGoHome()
        elif option == 5:
            patient.showAllPatient()
        elif option == 6:
            patient.ReverseTheLine()
        elif option == 7:
            print(f"Exited the Waiting Room")
            break


**Assignment Part 2: Stack**

Linked List based Stack is implemented in the following cell.

class Node:
  def __init__(self,elem=None,next=None):
    self.elem = elem
    self.next = next

class Stack:
  def __init__(self):
    self.__top = None

  def push(self,elem):
    nn = Node(elem,self.__top)
    self.__top = nn

  def pop(self):
    if self.__top == None:
      #print('Stack Underflow')
      return None
    e = self.__top
    self.__top = self.__top.next
    return e.elem

  def peek(self):
    if self.__top == None:
      #print('Stack Underflow')
      return None
    return self.__top.elem

  def isEmpty(self):
    return self.__top == None
st = Stack()
st.push(4)
st.push(3)
st.push(5)
st.push(1)
st.push(9)

print('Peeked Element: ',st.peek())
print('Popped Element: ',st.pop())
print('Popped Element: ',st.pop())
print('Popped Element: ',st.pop())
print('Peeked Element: ',st.peek())
print('Popped Element: ',st.pop())
print('Popped Element: ',st.pop())
print('Peeked Element: ',st.peek())
print('Popped Element: ',st.pop())
print(st.isEmpty())

You can print your stack using this code segment

def print_stack(st):
  if st.isEmpty():
    return
  p = st.pop()
  print('|',p,end=' ')
  if p<10:
    print(' |')
  else:
    print('|')
  #print('------')
  print_stack(st)
  st.push(p)

# st = Stack()
# st.push(4)
# st.push(3)
# st.push(5)
# st.push(1)
# st.push(9)
# print_stack(st)
# print('------')

Task 1: Diamond Count

def diamond_count(stack,string):
    #TO DO
    counter = 0
    for i in range(len(string)):
        if string[i]=="<":
          stack.push(string[i])
        elif string[i]==">":
            if stack.isEmpty() == False:
                s=stack.pop()
                counter+=1
    return counter
print('Test 01')
stack = Stack()
string = '<..><.<..>> '
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 3
print('-----------------------------------------')


print('Test 02')
stack = Stack()
string = '<<<..<......<<<<....>'
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 1
print('-----------------------------------------')

print('Test 03')
stack = Stack()
string = '>>><...<<..>>...>...>>>'
returned_value = diamond_count(stack,string)
print(f'Number of Diamonds: {returned_value}') #This should print 3
print('-----------------------------------------')

Task 2: Tower of Blocks

def remove_block(stack, n):
  #TO DO
    count = 0
    stk = Stack()

    while count<n-1:
      p = stack.pop()
      stk.push(p)
      count+=1
    p = stack.pop()
    while stk.isEmpty() is False:
        k = stk.pop()
        stack.push(k)




print('Test 01')
st = Stack()
st.push(4)
st.push(19)
st.push(23)
st.push(17)
st.push(5)
print('Stack:')
print_stack(st)
print('------')
remove_block(st,2)
print('After Removal')
print_stack(st)
print('------')

print()
print('======================================')
print()

print('Test 02')
st = Stack()
st.push(73)
st.push(85)
st.push(15)
st.push(41)
print('Stack:')
print_stack(st)
print('------')
remove_block(st,3)
print('After Removal')
print_stack(st)
print('------')

print()
print('======================================')
print()

Task 3: Stack Reverse

def conditional_reverse(stack):
    #To Do
    stk = Stack()
    while stack.isEmpty() is False:
      p = stack.pop()
      if stk.peek() != p:
        stk.push(p)
    return stk



print('Test 01')
st=Stack()
st.push(10)
st.push(10)
st.push(20)
st.push(20)
st.push(30)
st.push(10)
st.push(50)
print('Stack:')
print_stack(st)
print('------')
reversed_stack=conditional_reverse(st)
print('Conditional Reversed Stack:')
print_stack(reversed_stack) # This stack contains 50, 10, 30, 20, 10 in this order whereas top element should be 10
print('------')
