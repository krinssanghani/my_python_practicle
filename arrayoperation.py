from array import array

#1.-len() - Number of elements
arr=array('i',[10,20,30,40,50])
print(len(arr))

#2.-append(x) - Add element at End 
arr=array('i',[10,20,30])
arr.append(40)
print(arr)

#3.-insert(pos,x) - insert at Position
arr=array('i',[10,20,40])
arr.insert(2,30)
print(arr)

#4.-remove(x) - Remove first occurrence
arr=array('i',[10,20,30,20,40])
arr.remove(20)
print(arr)

#5.-remove and return last element
arr=array('i',[10,20,30,40])
x=arr.pop()
print("Removed:",x)
print(arr)

#6.-index(x) - Find Index of Element
arr=array('i',[10,20,30,40])
print(arr.index(30))

#7.-count(x) - count occurrences
arr=array('i',[10,20,30,20,40])
print(arr.count(20))

#8.-reverse() - Reverse array
arr=array('i',[10,20,30,40])
arr.reverse()
print(arr)