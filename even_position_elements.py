arr = [2,5,6,7,3,8,7,6,7,8,89,45,67]
print("The elements at the even positions in the given array are: ")
for i in range(0,len(arr)):
    if(i%2==0):
     print(arr[i],end=" ")