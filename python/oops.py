#oops
class Student:
    name="xyz"
    age=0
    def study(self):
        print("study 3 hour",self.name)

obj=Student()
obj.study()

#second program.
class Student:
    name="xyz"
    age=0
    def study(self):
        print("study 3 hour")

    def sleep(self):
        print("sleep 1 hour")
obj=Student()
obj.study()

#inheritance
#multiple.
class A:
    def show(self):
        print("This is show method")

class B(A):
    pass

class C(A):
    pass

#hybrid..
class A:
    def show(self):
        print("This is show method")

class B(A):
    def demo(self):
        print("demo method")

class C(A):
    pass

class D(B,C):
    pass

obj=C()
obj.show()
obj.demo() #error'''

#polymorphism.
#method overloading-not perform in python..
def setData(id,name):
    print("id,name")

def setData(id,name,age):
    print("id,name,age")
setData(101,"nikhil",20)  

def sum(a,b,c):
    print(a+b+c)
    
sum(10,20,30)
sum(10,20)#type error'''

def sum(a,b,c=0):#run because of default parameter..
    print(a+b+c)
    
sum(10,20,30)
sum(10,20)

#method overriding:-Polymorphism lets us define  methods in the child class that have the same name as the method in the parent class.
# In Interitance the child class inherits the methods from the parent class. However, it is possible to modify a method in a child class that it has inherited from the parent class. 
# This is particularly useful in cases where the method inherited from the parent class doesn't quite fit the child class. 
# In such cases, we re-implement the method in the child class. 
# This process of re-implementing a method in the child class is known as Method Overriding.
    
    
class Bird:
    def intro(self):
        print("there  are many types of birds")
        
    def flight(self):
        print("most of the birds can fly but some cannot")
        
class sparrow(Bird):
    def flight(self):
        print("i can fly")

class ostrich(Bird):
    def flight(self):
        print("i can't fly")
        
obj=sparrow()
obj.flight()

#Encapsulation.
class A:
    __name="abc"
    
class B(A):
    def show(self):
        print("this is show method",self.name)
    obj=B()
    obj.show()
    
    