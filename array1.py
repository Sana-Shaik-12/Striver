import numpy as np
import ast
def rowm(matrix, r,c,i):
    for k in range(c):
        if matrix[i][k]!=0:
            matrix[i][k]=-1
def colm(matrix, r,c,j):
    for k in range(r):
        if matrix[k][j]!=0:
            matrix[k][j]=-1

def findzero(matrix,r,c):
    for i in range(r):
        for j in range(c):
            if matrix[i][j]==0:
                rowm(matrix,r,c,i)
                colm(matrix,r,c,j)
                
    for i in range(r):
        for j in range(c):
            if matrix[i][j]==-1:
                matrix[i][j]=0
    
    print(matrix)            

if __name__ == "__main__":
    inpmat=input("enter")
    inpmat=ast.literal_eval(inpmat)
    matrix=np.array(inpmat)
    r,c = matrix.shape
    
    findzero(matrix,r,c)