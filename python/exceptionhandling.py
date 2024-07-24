print("Line 1 ")
print("Line 2 ")
print("Line 3 ")
print("Line 4 ")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

try:
    print(num1/num2)
    open("NIKHIL.txt")
    
except (ZeroDivisionError,FileNotFoundError):
    print("something went wrong")
print(" line 5")



#handle multiple exception..
print("Line 1 ")
print("Line 2 ")
print("Line 3 ")
print("Line 4 ")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

try:
    print(num1/num2)
    open("NIKHIL.txt")
    
except :
    print("something went wrong")
print(" line 5")

#finally..
print("Line 1 ")
print("Line 2 ")
print("Line 3 ")
print("Line 4 ")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

try:
    print(num1/num2)
   
    
except :
    print("something went wrong")
else:
    print("else block")

finally:
    print("finally block")
print(" line 5")