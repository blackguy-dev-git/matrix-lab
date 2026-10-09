import numpy as np
matrics1 = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
matrics2  = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])
def add_matrices():
    result = matrics1 + matrics2
    print(result)

def sub_matices():
    result = matrics1 - matrics2
    print(result)

def mul_matrices():
    result = matrics1 @ matrics2
    print(result)

def dev_matrices():
    result = matrics1 / matrics2
    print(result)

def nullornot():
    if np.all(matrics1 == 0):
        print("Matrix 1 is a null matrix")
    else:
        print("Matrix 1 is not a null matrix")
    if np.all(matrics2 == 0):
        print("Matrix 2 is a null matrix")
    else:
        print("Matrix 2 is not a null matrix")

def diagonalornot():
  
    if np.all(matrics1 == np.diag(np.diagonal(matrics1))):
        print("Matrix 1 is a diagonal matrix")
    else:
        print("Matrix 1 is not a diagonal matrix")
    if np.all(matrics2 == np.diag(np.diagonal(matrics2))):
        print("Matrix 2 is a diagonal matrix")
    else:
        print("Matrix 2 is not a diagonal matrix")

use = input("what u want to perform on matrices")
if use == "add":
    add_matrices()
elif use == "subtract":
    sub_matices()
elif use == "multiply":
    mul_matrices()
elif use == "divide":
    dev_matrices()
elif use == "null":
    nullornot()
elif use == "diagonal":
    diagonalornot()
else:
    print("Invalid operation")
