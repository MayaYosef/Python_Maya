# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:00:47 2020

@author: micha
"""

import numpy as np

def make_filters():
    #the func make a random matrix in size 3X3 and return it
    filter = np.random.rand(3,3)
    rows_f = filter.shape[0]
    cols_f = filter.shape[1]
    for i in range(rows_f):
        for j in range(cols_f):
            filter[i, j] = filter[i, j] * 5 #random numbers from 0.0 to 5.0
    return filter

def mult_matrix(a, filter):
    #the func gets two matrices and do a multiplication.
    #the func returns the result     
    rows_a = a.shape[0]
    cols_a = a.shape[1]   
    new_matrix = np.zeros(shape=(rows_a-2, cols_a-2)) 
    rows_matrix = new_matrix.shape[0] #rows of matrix
    cols_matrix = new_matrix.shape[1] #columns of matrix
    for i in range(rows_matrix):
        for j in range(cols_matrix):
            new_matrix[i, j] = sum_of_numbers(np.dot(a[i:i+3, j:j+3], filter))
        #(  if a at first was in size 9X9 and not 8X8 then at the end a was in size 3X3 
        #and then i+3 or j+3 was not within the boundaries of a
        #instead of line 30 I would write:
        #if rows_a ==3 and cols_a ==3:
            #new_matrix[i, j] = sum_of_numbers(np.dot(a, filter))
        #new_matrix[i, j] = sum_of_numbers(np.dot(a[i:i+3, j:j+3], filter))  )
    return new_matrix

def sum_of_numbers(matrix):
    #the func gets a matrix and adds the numbers in it
    #the func returns the sum
    rows_matrix = matrix.shape[0]
    cols_matrix = matrix.shape[1]
    sum = 0; #the sum of the numbers
    for i in range(rows_matrix):
        for j in range(cols_matrix):
            sum = sum + matrix[i, j]
    return sum        
    
def main(): 
    a = np.array([[0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0]]) #matrix in size 8X8
    filter = make_filters() #a random matrix in size 3X3
    rows_f = filter.shape[0] #rows of filter
    cols_f = filter.shape[1] #columns of filter
    a = mult_matrix(a, filter)
    rows_a = a.shape[0] #rows of a
    cols_a = a.shape[1] #columns of a
    print(a)
    while rows_a >= rows_f and cols_a >= cols_f:
        filter = make_filters()
        a = mult_matrix(a, filter)
        rows_a = a.shape[0]
        cols_a = a.shape[1]
        print(a)

if __name__ == "__main__": 
    main()        
