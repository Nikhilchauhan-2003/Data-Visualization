#file handling.

'''#creating file.
file=open("NIKHIL.txt",'w')
file.write("This is Python class.and today We are learning file handing")
file.close()


#reading
file=open("NIKHIL.txt",'r')
data=file.read()
print(data)
file.close()

file=open("NIKHIL.txt",'r')
print(file.tell())
data=file.read(7)
print(data)
print(file.tell())
file.close()


#seek method - change postion of cursor or  file pointer to read data.
file=open("NIKHIL.txt",'r')
print(file.tell()) 
file.seek(12)
data=file.read(5)
print(data)
print(file.tell())
file.close()'''

'''#Pickle module is used to r/w from binary file. Stores data in same format as in the memory.
import pickle
file=open("pickle.dat",'wb')
li=[10,20,30,40,50]
pickle.dump(li,file)
file.close()

import pickle
file=open("pickle.dat",'rb')
data=pickle.load(file)
print(data)
file.close()'''

#csv file
import csv
f=open("Nikhil.csv",'a',newline="")
wo=csv.writer(f)
data=[["a","b","c","d"],[16,14,12,10],[26,24,22,20],[36,34,32,59]]
wo.writerows(data)
f=open("Nikhil.csv",'r')
re=csv.reader(f)
li=list(re)
for i in li:
    print(i)
f.close()