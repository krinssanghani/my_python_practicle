from array import array

#Ex-1. - positive Indexing
arr=array('i',[10,20,30,40,50])
print(arr[0])   #first element
print(arr[2])   #third element
print(arr[4])   #fifth element

#Ex-2. - negative Indexing
arr=array('i',[10,20,30,40,50])
print(arr[-1])   #last element
print(arr[-2])   #second element
print(arr[-5])   #first element

#ex-3. - modifying elements using index
arr=array('i',[10,20,30,40,50])
arr[2]=35
print(arr)
