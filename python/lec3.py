#display a list
list=[27,30,40,'hello']

print(list) #completelist.
print(*list) #without any formating.

'''#3- Accesing members using for loop-  (can not use to display alternate menbers ...can only display every element in new line  and --can also used to count elemets)
                                           (cannot used to raverse element in reverse order)
         -for variable in listname:
              #code/working
--Indexing of list- (created by system due to which element in list it get inserted in orderd (i.e. insertion orderd))'''


#fecting

l=[10,20,30,40,50,60,70,80,90,100,110]
print("3rd element:",l[2])
print("4th element from last : ",l[-4])
#fetching element from 3rd to 10th position 

print("element to 3rd position from 10th position :", l[2:10])
print("alternate element from 3rd to 10th:",l[2:10:2])

#print the element in backward direction using forward direction.
l=[1,2,3,4,8,6,4,9,0,12,34,5,6,22,24,25,26,27,28,29]
print(l[19::-1])

print("--------------------------------------------------")

n=len(l)-1
for i in range(n,-1,-1):
    print(l[i],end=",")
    
print("--------------------------------------")
#inserting element in list:

l=[20,30,12,12,5,78,90]
l2=[1,2,3]
l3=[12,52,62]
x=int(input("enter any number:")) #append method
l.append(x)#append method
print("update list is:",l)
l.append(l2)
print("merged list:",l)
#extend()method
l.extend(l3)
print(l)

print("----------------------------------------")

# 2- Insert at specified postion-
l=[20,50,12,12,85,48,12,63,17,12,82,15,20,75,25,12,48,63,60,90]
l.insert(5,3)
print(l)

print("---------------------------------------------")

#find a method to insert all the element of another sequence datatype at articular index in the list.but all the elements must be inserted one by one.

