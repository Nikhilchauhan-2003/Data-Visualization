student = {"stdid":"std101","stdname":"ashish kumar","standard":"10th","age":"15","hindi":"67","english":"89"}
print(student)

print("_---------------------------------")

student.pop('hindi')
print(student)


#pop
student.popitem()
print(student)

#keys()
elementkeys=student.keys()
print(elementkeys)

#values()
elementvalues=student.values()
print(elementvalues)

#items()
elements=student.items()
print(elements)

#get()
x= student.get('maths')
print(x)

#get()-return specoified keys.#
x= student.get('maths','no element exist')
print(x)

#update():    update or insert multiple element(in tghe key-value pair) in the dict.(2nd dict in 1st)

print('-----------------------------')
student1= {"stdid":"std101","stdname":"ashish","standard":"10th","age":"15"}
student2 = {"stdid":"std102","stdname":"kumar","standard":"10th","age":"19","hindi":"67","english":"89"}
student1.update(student2)
print(student1)

#fromkeys()--return a dict with specified keys and value
print("----------------------------------")
x=student1.fromkeys('standard','stdname')
print(x)

print("------------------------------------")
print("------------------------------")
x=student1.fromkeys(student1.keys(),student1.values())
print(x)

print("--------------------------------------")
print("_--------------------------------------------")
x=student1.fromkeys(student1.keys(),15)
print(x)


print("----------------------------------")
print("--------------------------------")
#len()
x=len(student1)
print(x)
