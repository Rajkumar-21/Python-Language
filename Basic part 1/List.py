# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 20:42:24 2020

@author: Rajkumar
"""
# List creation

my_list=[1,2,3,4,5,6,7,8,9,10]

print(my_list)

print(len(my_list))

# Indexing and Slicing

print(my_list[1])

print(my_list[1:7:2])

print(my_list + ['one','two','three'] + ['four','five','six'])

# Append in List 

print(my_list)

my_list.append('Append element')

print(my_list)

my_list.pop()

print(my_list)

my_list.pop(-1)

print(my_list)

my_list.remove(1)

print(my_list)

new_list = ['s','g','r','y','a','e','b','q']

new_list.sort()

print(new_list)

new_list.reverse()

print(new_list)

# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]

print(matrix)

# Grab first item in matrix object
print(matrix[0])

# Grab first item of the first item in the matrix object
print(matrix[0][0])

# Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix]

print(first_col)

