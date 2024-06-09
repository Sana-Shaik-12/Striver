import numpy as np
import ast
def findzero(matrix,r,c):
    print("initial matrix",matrix)
    row = [0]*r
    col = [0]*c
    for i in range(r):
        for j in range(c):
            if matrix[i][j]==0:
                row[i]=1
                col[j]=1
                
    for i in range(r):
        for j in range(c):
            if row[i] or col[j]:
                matrix[i][j]=0

    print("final matrix",matrix)          

if __name__ == "__main__":
    inpmat=input("enter")
    inpmat1=ast.literal_eval(inpmat)
    matrix=np.array(inpmat1)
    r,c = matrix.shape
    
    findzero(matrix,r,c)