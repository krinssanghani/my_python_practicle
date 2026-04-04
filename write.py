#1. write() - write a single string
f=open("one.txt","w")
f.write("Hello students\n")
f.write("welcome to pythone file handling\n")
f.write("learnig is fun\n")
f.close()


#2.old data erased
f=open("one.txt", "w")
f.write("new content only.\n")
f.close()


#3.apeend mode ("a") example(old data kept)
f=open("one.txt","a")
f.write("this line added at the end.\n")
f.close()


#4.writelines() - write multiple lines
f=open("one.txt","w")
lines=[
"python programming\n",
"file handling\n",
"error handling\n",
"exception handling\n"
]
f.writelines9(lines)
f.close()