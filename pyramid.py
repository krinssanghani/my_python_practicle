#1 : 
n = int(input("enter number of lines:"))
for i in range(1, n + 1):
    print("*" * i)


#2 :
for i in range(1,4):
    print("*" * i)


#3 :
n=5
for i in range(1, n+1):     #line number
    for j in range(1, i+1): #printing the numbers
        print(j,end="")
    print()


#4 :
n = int(input("enter number of lines:"))
i=1
while i<=n:
    print("*" * i)
    i += 1


#5 :
n = int(input("enter number of lines:"))
i=n
while i>=1:
    print("*" * i)
    i -= 1