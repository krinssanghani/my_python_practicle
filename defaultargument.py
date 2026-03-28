#1.
def greet(name="Guest"):
    print("Hello",name)
greet("Alice")
greet()

#2.
def add(a,b=5):
    print("sum:",a+b)
add(10,20)
add(10)

#3. square of number
def sqr(num,exp=2):
    return num**exp
print(sqr(3))  #uses default exp=2
print(sqr(3,3)) #overrides default
print(sqr(2,4))