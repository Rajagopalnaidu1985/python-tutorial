
###### CLASS #####

class computer:
    def config(self):
        print("i5, 16gb, 2TB")

com1=computer()
com2=computer()

computer.config(com1)
computer.config(com2)

com1.config()
com2.config()


#### Example #####

class detail():
    def human(self):
        print("name:Raja, hight:170cm, weight:75kg, colour:Brown")

info1=detail
info2=detail

detail.human(info1)
detail.human(info2)

info1.human()
info2.human()





### DURGA ###

class Student:
    '''This is demo class'''  # Doc string
    #variables (Properties) like names, marks,roll no
    # Methods (Actions/beheaviour) like read, write, eat, sleep, talk



## to access the doc string below are working:

print(Student.__doc__)

or
help(Student)


every object has properties and behaviour.
properties (Data) are specified by variabls.
behaviour can be specified by methods.

Types of veriables:
1) Instence veriables (Object level variables)
2) Static variables (Class level veriables)
3) Local variables (Method level veriables)


# 3types of methods allovable inside of class:

1) Instence methods
2) Class methods
3) Static methods

### class, object, Reference variable

#Class:- Class is bule print/Plan/model/Design for an Objects. 

        #Class contains Variables & Methods which are required for every object.


#Object:- is a physical existence of a class. 
        #from a class we can create multiple objects.

#Reference variable: The variable which can be used to refer object.

                    #Byusing this variable we can operate object i.e by using reference 
                    #variable we can access variables and methods.


### How to create object in python ###

Reference variable = class name()


Example:

class Student:
    def __init__(self):
        self.name = "Raja"
        self.rollno = 102
        self.marks = 89
    def talk(self):
        print("helow my name is :", self.name)
        print("my rollno is :", self.rollno)
        print("my marks are:",self.marks)

s=Student()
print("Student name:", s.name)
print("Student rollno:", s.rollno)
print("Student marks:", s.marks)
s.talk()



#Example2: 

class Student():
    def __init__(self, name, rollno, marks): #constructor
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def talk(self):     #Instence method
        print("Myname is :", self.name)
        print("Rollno is:", self.rollno)
        print("Marks are:", self.marks)

s1=Student("Rama", 102, 78)
s2=Student("Krishna", 103, 98)
s3=Student("Sita", 104, 99)
print(s1.name, s1.rollno, s1.marks)
print(s2.name, s2.rollno, s2.marks)
print(s3.name, s3.rollno,s3.marks)

###Result is :
print(s1.name, s1.rollno, s1.marks)
Rama 102 78
>>> print(s2.name, s2.rollno, s2.marks)
Krishna 103 98
>>> print(s3.name,s3.marks, s3.rollno)
Sita 99 104






####################### SELF ###############################

1) self is a reference variable, which is always pointing to current object.
    with in the python class, to access current object we can use self.
2) The first argument for the constructor should be "Self"    
    The first argument for the instence method is always "Self"
    We are not required to provide value for self variable, PVM it self will provide value for it.
    
3)  we can use 'self' always with in the class only.
    Inside constructor, we can use self to declare object related variables(instence variables)   
    -> Inside instence method, we can use self to access the values of instence variables.

4) self is not a key word we can use any name like 'kelf' , 'delf'etc.
    but it is recomended to use self.








class Team():
    def __init__(self):
        print(id(self))

t = Team
print(id(t))




###################### Constractur (__init__) ########################

1) Constructor is a special method.
2) The name of the constructure is always __init__()
3) we are not required to call constructure explicitly. It will be excuted automatically 
when we are creating an object.
4) Per object constructer will excuted only once
5) The main purpose of constructor is to declare and initalise instance variables
   __init__ means initilazation
6) Constructor should have at least 1 aregument i.e self to refer current object
7) With in python class constructor is optional. If we are not providing constructor (i.e __init__) default constructur will be provided by PVM.
8) We can call constructor explicitly, then it will be excuted just like a normal method
    and new object wont be created.
9) Constructor or Method over loading is not possible in Python.
    If we are trying to declare multiple constructor PVM will always consider only last constructor.



class Test:
    def __init__(self):
        print("constructure excution")

t1=Test()
t2=Test()
t3=Test()








###### Excution  ######

####### Requirement ###
#Movie class
#Create multiple objects
#Add created objects to the list 
#Try to get these objects from list one by one
#invoke movie class functionality on that object




###### Excution  ######
class Movie:
    '''Checking for the movies list which are available.'''
    def __init__(self, title, hero, heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine
    
    def info(self):
        print('Movie name:', self.title)
        print('Movie hero:', self.hero)
        print('Movie heroine:', self.heroine)

list_of_movies = []
while True:
    title = input("Enter movie name: ")
    hero = input("Enter hero name: ")
    heroine = input("Enter heroine name: ")
    m = Movie(title, hero, heroine)
    list_of_movies.append(m)
    print("Movie added to the list successfully")
    option = input('Do you want to add one more movie [Yes|No]: ')
    if option.lower() == 'no':
        break

print('All Movies Information:')
print('#' * 40)
for movie in list_of_movies:
    movie.info()
    print()


    




  









