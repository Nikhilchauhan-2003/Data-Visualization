#tuple
a=10,200,30
print(a)
print(id(a))

a=10,300,30
print(a)
print(id(a))

#set
months=["jan","feb","mar","apr","jan"]
print(months)
months=set(months)
print(months)
print(len(months))

print("-------------------------------------------------")

months={"jan","feb","mar","apr"}
print(months)
months.add("may")
months.update(["june","july","aug","sep","oct","nov","dec"])
print(months)

print("------------------------------")
months={"jan","feb","mar","apr"}
print(months)
months.discard("mar")
print(months)

print("---------------------")
months={"jan","feb","mar","apr"}
print(months)
months.remove("mar")
print(months)




print("-----------------------")
#string....

name="nikhil"
print(name)
name+"chauhan"
print(name)

print("-------------------------")
name="Nikhil"
print(id(name))
name=name+"Chauhan"
print(id(name))


#slicing
print("------------------------")
name="I am Java Trainer"
print(name)
print("name[2:4]",name[2:4])
print("name[5:9]",name[5:9])
print("name[:15]",name[:15])
print("name[2:]",name[2:])
print("name[:]",name[:])
print("name[0:7:3]",name[0:7:3])
print("name[::]",name[::])
print("name[::-1]",name[::-1])

#operators
x=["apple","banana"]
y=["apple","banana"]
z=x
print(x is z)
print(x is y)# it can specify the object not value.


#capitalize
print("------------------------------------")
str="nikhil chauhan"
print(str)
print(id(str))
str=str.capitalize()
print(str)
print(id(str))

#center
print("-------------------")
str="nikhil"
print(str)
str=str.center(15)
print(str)

print("-------------------")
str="nikhil"
print(str)
str=str.center(15,'*')
print(str)

#center method()--it allign string to the center by filling padding right and left of the sting.this method take two parameter,first is a width and a second is a fillchar which is optional.The fillchar is a character which is used to fill the left and right padding of the string..
str="HELLO"
str=str.center(20)
print(str)

#count.
str=" second a start index and third "
oc=str.count('a',8,15)
print(oc)

str="ab bc ca de ad da ab bc ca"
oc=str.count("a",3,8)
print(oc)

#endwith
str="second a start index and third"
isends=str.endswith('third')
print(isends)

str="hello this is python class"
ksends=str.endswith('nd',0,6)
print(ksends)

#find()-find substring in the whole string and return index of the first match..it return-1 if substring does not match..
str="welcome to the python class"
str2=str.find("t")
str3=str.find("t",20,25)
print(str2)
print(str3)

#index() -  helps you find the index position of an element or an item in a string of characters or a list of items.
str="second a start index and third"
str2=str.index('a')
print(str2)
str3=str.index('a',9,13)
print(str3)

#isalnum() - aplha numeric -returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
str="1235421521515"
print(str.isalnum())

#isalpha() - 
str="second a start index and third"
print(str.isalpha())

#isnumeric() - 
str="1235421521515"
print(str.isnumeric())

#lstrip()-is used to remove all the leading character from the string.
#rstrip()-used to return a new string by removing the trailing characters (based on the argument passed) from the input string.

str=".....nikhil....."
str1=str.lstrip('.')
str2=str.rstrip('.')
str3=str.strip('.')
print(str1)
print(str2)
print(str3)

#replace()
str="java is a programming language"
str=str.replace("java","c")
print(str)

#swapcase() - returns a string where all the upper case letters are lower case and vice versa.
str="java is a programmming language java"
str=str.swapcase()
print(str)









