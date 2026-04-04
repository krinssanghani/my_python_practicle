#1.
try:
    number1=int(input("enter the number :"))
    number2=int(input("enter another number :"))
    result = number1 / number2
    
except ZeroDivisionError:
    print("You cannot divide by zero")
    
except ValueError:
    print("please enter a valid number")
    
else:
    print("division successfully! result is :",result)
    
finally:
    print("this block always runs")
    
    
#2.
try:
    my_list=[1,2,3]
    print(my_list[1])  #this index does not exist
    
except IndexError:
    print("Index is out of range!")
    
else:
    print("Element found successfully!")
    
finally:
    print("program finished.")