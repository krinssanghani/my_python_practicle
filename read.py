#1. read() method
f=open("one.txt","r")
data=f.read()
print("file content: " ,data)
f.close()

#2. reading specific number of characters from a file using read()
f=open("one.txt","r")
data=f.read(10)
print("file part : ",data)
f.close()

#3. readline()-read one line
f=open("one.txt","r")
line1=f.readline()
line2=f.readline()
line3=f.readline()
print("line 1:",line1)
print("line 2:",line2)
print("line 3:",line3)
f.close()

#4. Reading specific line from a file using readlines()
f=open("one.txt","r")
lines=f.readlines()
print(lines[1].strip())
f.close()