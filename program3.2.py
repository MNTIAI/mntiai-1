import numpy as np
A = np.array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8]])
#Print matrix A
print ("\n The matrix A is \n",A)
# Print square of each element of A
print("\n Square of matrix A \n",A**2)
# Print cube of each element of A
print("\n Cube of matrix A \n",A**3)
#To find square root of each element of A
sqrt_A =np.sqrt(A)
print("\n The square of each element of A is\n",sqrt_A)

# Add .5 to each entry in row-0 (Slicesreturn arrays of A
print(0.5 + A[0, :])
B = np.array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8]])
#Print matrix B
print ("\n The matrix B is \n",B)
print("The sum tarts from here....\n")
C=A+B
print("\n The sum of A and B is \n",C)
print("\nThe sum of A and B is\n",np.add(A,B))
print("\n The multiplication begins fromhere..\n")
Sca_M=A*B
print("\n The product of A and B is\n",Sca_M)
print("\n The sum of elements of Matrix A is=", np.sum(A))
print("\n The average of elements of MatrixA is =", np.mean(A))
print("\n The standard deviation of elementsof Matrix A is =", np.std(A))
print("\n The variance of elements of MatrixA is =", np.var(A))
print("\n The maximum of elements ofMatrix A is =", np.max(A))
print("\n The minimum of elements ofMatrix A is =", np.min(A))
print("\n The order of the matrix A\n",A.shape)
print("\n The number of element of thematrix A\n",A.size)
print("\n Returns class type \n",type(A))
print("\n Returns\n",A[0,1:])
print("\n Returns \n",A[:2,:2])
print("\n Return\n",A[2:,2:])
print("\n Returns \n",A[1:3,1:2])