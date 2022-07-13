A = [[51, 9, 7],  
     [20, 4, 5],  
     [43, 7, 91],  
     [2, 10, 39]]  
  
transResult = [[0, 0, 0, 0],    
               [0, 0, 0, 0],  
               [0, 0, 0, 0]]  
# Use nested loop  
for a in range(len(A)):    
   for b in range(len(A[0])):    
          transResult[b][a] = A[a][b] # store transpose result on empty matrix          
# Printing result  
print("The transpose of matrix A is: ")  
for res in transResult:    
   print(res)  