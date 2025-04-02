'''Write a program to create a set and perform the following operations on that set-
 1. Create a set with integer elements 
 2. Create a set with mixed data type elements
 3. Create another set with elements - 1, 2, 3, 4, 3, 2 
 4. Create a set from a list with elements - [1, 2, 3, 2]
 5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5'''


set1 = {1 , 2 , 3 , 3 , 4 , 5 , 5}
print(set1)
set2 = {'Advika' , 3 , 3 , True , 5.0 , 5.0}
print(set2)
set3 = {1 ,2 ,3 ,4 ,3 ,2}
print(set3)
list1 = [1,2,3,2]
s1 = set(list1)
print(s1)
list2 = [0 , 1 , 3  , 4 , 5 ]
list2.pop(0)
print(set(list2))
