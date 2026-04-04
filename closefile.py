#1. manually closing
f=open("one.txt","r")
f.close()

#2.using with statement
with open("one.txt","r") as f:
    content=f.read()
    print(content)