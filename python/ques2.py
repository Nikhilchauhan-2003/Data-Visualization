
# display no btw 10 to 500 which is divisible by 7 and 10.
'''for i in range(10,500):
    if(i%5==0 and i%7==0 and i%10==0):
        print(i)'''
        
        
# count the no.btw 100 to 1000 which is even and divisible by 3.
count=0
for i in range(100,1000):
    if (i%2==0 and i%3==0):
        print(i,end=",")
        count= count+1
print("total no:",count , end=",")