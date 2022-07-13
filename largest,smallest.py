arr = [23,22,34,12,78,45,30]

max = arr[0]

for i in range(0,len(arr)):
    if(arr[i] > max):
        max = arr[i]

print("The largest element in the array is:" +str(max));

min = arr[0]

for i in range(0,len(arr)):
    if(arr[i] < min):
        min = arr[i]
print("The smallest element in the array is :" +str(min));        