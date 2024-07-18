#tuple
numbers=(23,45,67,89,13)
#print the tuple
print (numbers)
print(*numbers)
print("-----------------------------------")

for element in numbers: 
    print(element,end=",")
    
    
print("---------------------------")
print(numbers[-5::])
print(numbers[4::-1])#slicing
n=len(numbers)-1 #backward indexing..
for i in range(n,-1,-1):
    print(numbers[i],end=",")


