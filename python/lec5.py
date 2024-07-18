#dictionary
student = {"stdid":"std101","stdname":"ashish kumar","standard":"10th","age":"15"}
print(student)

student['standard']='12th'
student['hindi']=78
print(student)

for element in student:
    print(element)
    
print("-----------------------")
#print in formate..
for key in student:
    print(key,"-",student[key])
    
print("------------")
#for finding value.
for key in student:
    print(student[key])
    
print("------")
print("marks of hindi:",student['hindi'])




