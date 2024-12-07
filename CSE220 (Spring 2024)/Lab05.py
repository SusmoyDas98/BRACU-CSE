#Assignment 05

import numpy as np
import math

#------------------------------------------------------------------------------------------------------------------------------

#Run this cell
class Node:
  def __init__(self, elem, next = None):
    self.elem = elem
    self.next = next

def create_linked_list(arr):
  head = Node(arr[0])
  tail = head
  for i in arr[1:]:
    new_node = Node(i)
    tail.next = new_node
    tail = new_node
  return head

#------------------------------------------------------------------------------------------------------------------------------

#Very Easy

#a)
def recursive_sum(arr):
    if len(arr) == 0 : return 0
    elif  arr[0] > 0 and  arr[0] % 2 == 0:
        return arr[0] + recursive_sum(arr[1::])
    else:
        return recursive_sum(arr[1::])
arr1 = np.array([10,34,-8,1,5,6])
returned_value = recursive_sum(arr1)
print(f'Sum of even positive elements of an array: {returned_value}') # This should print 50

#------------------------------------------------------------------------------------------------------------------------------

#b)
def recursive_multiply(head):
    if head == None: return 1
    elif head.elem % 2 != 0 and head.elem>0:
        return head.elem*recursive_multiply(head.next)
    else:
        return recursive_multiply(head.next)
arr1 = np.array([10,3,-9,1,5,6])
head= create_linked_list(arr1)
returned_value = recursive_multiply(head)
print(f'Product of odd positive elements of a linked list: {returned_value}') # This should print 15

#------------------------------------------------------------------------------------------------------------------------------

#c)
def nCr(n,r):
    def factorial(x):
        if x==1: return int(1)
        else:
            return int(x*factorial(x-1))
    return  int((factorial(n))/((factorial(n-r))*(factorial(r))))
print('========1========')
returned_value = nCr(9,6)
print(f'9C6: {returned_value}') # This should print 84
print('========2========')
returned_value = nCr(8,2)
print(f'8C2: {returned_value}') # This should print 28
print('========3========')
returned_value = nCr(48,1)
print(f'48C1: {returned_value}') # This should print 48

#------------------------------------------------------------------------------------------------------------------------------

#d)
def count_digit_recursive(num):
    if int(num%10) ==  int(num):
        return 1
    else:
        return  1+count_digit_recursive(int(num//10))

returned_value = count_digit_recursive(7508)
print(f'Number of Digits: {returned_value}') # This should print 4

#------------------------------------------------------------------------------------------------------------------------------

#e)
def check_prime_recursive(num):
    def prime_checker(start,num):
        if start==num:
            return True
        elif num%start==0:
            return False
        elif num%start!=0:
            return prime_checker(start+1, num)
    return prime_checker(2,num)
print('========1========')
returned_value = check_prime_recursive(79)
print(f'Prime: {returned_value}') # This should print True
print('========2========')
returned_value = check_prime_recursive(391)
print(f'Prime: {returned_value}') # This should print False

#------------------------------------------------------------------------------------------------------------------------------

#f)
def recursive_print(head):
    c1 = head
    if c1 is None:
        return  None
    else:
        recursive_print(c1.next)
        print( c1.elem, end=" ")
arr1 = np.array([10,20,30,40])
head= create_linked_list(arr1)
recursive_print(head) #This should print 40  30  20  10

#------------------------------------------------------------------------------------------------------------------------------

#Easy

#a)
def dec_to_binary_recursive(n):
  if n==1 or n==0 : return n
  else:
    return str(dec_to_binary_recursive(n//2)) + str(n%2)
print('========1========')
returned_value = dec_to_binary_recursive(35)
print(f'Binary Number: {returned_value}') # This should print 100011
print('========2========')
returned_value = dec_to_binary_recursive(50)
print(f'Binary Number: {returned_value}') # This should print 110010

#------------------------------------------------------------------------------------------------------------------------------

#b)
def encoding(dec_number): #0<=dec_number<=15
  return '0123456789ABCDEF'[dec_number]
def dec_to_hexa_recursive(n):
    if n == 0 : return ''
    else:
        return str(dec_to_hexa_recursive(n//16))+str(encoding(n%16))


print('Use of encoding function')
decimal_number = 7
print(f'Hexadecimal Number: {encoding(decimal_number)}')
decimal_number = 13
print(f'Hexadecimal Number: {encoding(decimal_number)}')

print('========1========')
returned_value = dec_to_hexa_recursive(1230)
print(f'Hexadecimal Number: {returned_value}') # This should print 4CE
print('========2========')
returned_value = dec_to_hexa_recursive(600)
print(f'Hexadecimal Number: {returned_value}') # This should print 258

#------------------------------------------------------------------------------------------------------------------------------

#c)
def print_alphabets_recursive(head):
    c1 = head
    c2 = head
    def find_vowels(c1):
        if c1 is None: return ''
        elif c1.elem in "aeiouAEIOU":
            return c1.elem +" "+find_vowels(c1.next)
        elif c1.elem not in "aeiouAEIOU":
            return find_vowels(c1.next)
    def find_cons(c2):
        if c2 is None: return ''
        elif c2.elem not in "aeiouAEIOU":
            return  find_cons(c2.next)+" "+c2.elem
        elif c2.elem   in "aeiouAEIOU":
            return find_cons(c2.next)
    return find_vowels(c1)+find_cons(c2)

head = create_linked_list(np.array(['b', 'e', 'a', 'u', 't', 'i', 'f', 'u', 'l']))
print_alphabets_recursive(head) #This will print e a u i u l f t b

#------------------------------------------------------------------------------------------------------------------------------

#d)
def harmonic_sum(n):
    if n == 0: return 0
    else:
        return ((-1)**(n+1))/n + harmonic_sum(n-1)
print(f'Harmonic Sum(3): {harmonic_sum(3)}') #This should print 0.8333333333333333
print(f'Harmonic Sum(4): {harmonic_sum(4)}') #This should print 0.5833333333333333

#------------------------------------------------------------------------------------------------------------------------------

#Medium

#a)
def hoc_Builder(height):
    if height == 0 : return 0
    if height == 1 : return 8
    else:
        return 5+hoc_Builder(height-1)

print(f'Cards Needed: {hoc_Builder(4)}') #This should print 23
print(f'Cards Needed: {hoc_Builder(1)}') #This should print 8
print(f'Cards Needed: {hoc_Builder(0)}') #This should print 0

#------------------------------------------------------------------------------------------------------------------------------

#b)
def reach_goal(n):
    c = 0
    def counter(n, c):
        if n==1 : return c
        elif  n%2 == 0: return counter(n//2, c+1)
        elif  n%2 != 0: return counter((n*3)+1, c+1)
    return counter(n, c)

steps=reach_goal(21)
print(f'Number of steps to reach the goal: {steps}')  #This should print 7

#------------------------------------------------------------------------------------------------------------------------------

#Hard

#a)
def print_pattern(n):
    def pattern_printer(n):
        if n==0 or n<0:
            print(n,end=" ")
            return n+5

        else:
            print(n,end=' ')
            pattern_printer(n-5)
            print(n,end=' ')
    def print_row(n,c):
        pattern_printer(n)
        print()
        if n-5>0:
            print(c*"   ",end="")
            print_row(n-5,c+1)
    return print_row(n, 1)

print('========1========')
n = 16
print_pattern(n)
#This should print

#16 11 6 1 -4 1 6 11 16
#   11 6 1 -4 1 6 11
#      6 1 -4 1 6
#        1 -4 1

print('========2========')
n = 10
print_pattern(n)
#This should print

#10 5 0 5 10
#   5 0 5

#------------------------------------------------------------------------------------------------------------------------------

#b)
def merge_Lists(mid_list,final_list,combined_list):
    if mid_list == [] and final_list == [] : return combined_list
    elif mid_list!=[] and final_list == [] :
        combined_list.append(mid_list[len(mid_list)-1 ])
        return merge_Lists(mid_list[0:len(mid_list)-1:], final_list, combined_list)
    elif mid_list == [] and final_list != []:
        combined_list.append(final_list[len(final_list)-1])
        return merge_Lists(mid_list, final_list[0:len(final_list)-1:], combined_list)
    else:
        if mid_list[len(mid_list)-1] > final_list[len(final_list)-1]:
            combined_list.append(mid_list[len(mid_list)-1])
            return merge_Lists(mid_list[0:len(mid_list)-1:], final_list, combined_list)

        elif final_list[len(final_list)-1] > mid_list[len(mid_list)-1]:
            combined_list.append(final_list[len(final_list)-1])
            return  merge_Lists(mid_list, final_list[0:len(final_list)-1:], combined_list)

mid=[5, 7, 14, 20, 24]
final=[10, 12, 25]
merged_list=merge_Lists(mid,final,[])
print(merged_list)
# This should print [25, 24, 20, 14, 12, 10, 7, 5]

mid=[11, 20, 24, 28]
final=[10, 12]
merged_list=merge_Lists(mid,final,[])
print(merged_list)
# This should print [28, 24, 20, 12, 11, 10]

#------------------------------------------------------------------------------------------------------------------------------

#Very Hard

def flatten_List(given_list, output_list):
    if len(given_list) == 0 : return output_list
    if type(given_list[0] ) is not list:
        output_list.append(given_list[0])
        return flatten_List(given_list[1::], output_list)
    elif  type(given_list[0] ) is list:
        flatten_List(given_list[0], output_list)
        return flatten_List(given_list[1::], output_list)
given_list = [1, [2, [3, [4], 5], 6], 7, 8, [9, [[10, 11], 12], 13], 14, [15, [16, [17]]]]
output_list = flatten_List(given_list, []) # Initial empty list is sent for update
print(output_list)
#This should print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

#------------------------------------------------------------------------------------------------------------------------------

#Bonus Task

def number_of_ways(steps):
    if steps == 0 or steps == 1 : return 1
    if steps == 2 : return 2
    return number_of_ways(steps-1)+number_of_ways(steps-2)+number_of_ways(steps-3)
print(f'The number of ways you can climb the stairs: {number_of_ways(3)}') #This should print 4
print(f'The number of ways you can climb the stairs: {number_of_ways(5)}') #This should print 13
