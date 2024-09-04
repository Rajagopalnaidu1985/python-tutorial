
#### Functions ####

def greet():
    print("Hellow Baby")
    

def add(x,y,z):
    print(x+y+z)


def multiplication(a,b):
    print(a*b)


greet()
add(2,67,98)
multiplication(4,6)


###

def add(x,y):
    z=x+y
    print(z)

def multy(a,b):
    c=a*b
    print(c)

add(6,8) 
multy(4,5)




###

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d


result1,result2 = add_sub(4,9)
print(result1,result2)


###

### Arguments are 4 types###
#1) Position
#2) Keyword
#3) Default
#4) Veriable leanght

#1) position arguments
def person(name,age):
    print(name)
    print(age)

person("Raja", 16)

###

#2) Keyword arguments
def person(name,age):
    print(name)
    print(age)

person(age=16,name="Raja")


###

#3) Default arguments
def person(name,age=18): #if some social network websites requires min age is 18 and while enter age if user not provide it will through error. that is the case we ill use this
    print(name)
    print(age)

person("Raja") # if we give age then given age will over ride


# if we give age then given age will over ride
# example: 

def person(name,age =18): #if some social network websites requires min age is 18 and while enter age if user not provide it will through error. that is the case we ill use this
    print(name)
    print(age)

person("Raja", 30)



###

#3) Variable lenght arguments

def sum(a,b):
    c=a+b
    print(c)

sum(6,8)

## if arguments are having multiple values 

def sum(a, *b): # here *b argument alows multiple values 
    c=a+b
    print(c)

sum(6,8,12,45,23,33) # here 6 is allocated to "a" and remining all values are allocated to "b" 

# from above excution we will get error due to "a" type is 'int' and "b" type is 'tuple'
#to solve above

def sum(a, *b): # here *b argument alows multiple values 
    print(a) #value is 6
    print(b) #value is (8, 12, 45, 23, 33)

sum(6,8,12,45,23,33) #to just verify the arguments allocation printing the a,*b 


### to do actual excution for above problem

def sum(a, *b): # here *b argument alows multiple values 
    c=a
    print(c) # if we dont need all steps excution we can commit this line
    for i in b:
        c=c+i
        print(c) # if we dont need all steps excution we can commit this line
    print(c)

sum(6,8,12,45,23,33)



##### personal example to solve above similer problem with 3 argument values

def problem(a, *b):
    c=a
    for i in b:
        c=c+i
    print(c)

problem(4,12,15,2,8,9)    



##### Key word veriable lenght arguments #######

def person_details(name, *details):
    print(name)
    print(details)

person_details('Raja',16,'Hyderabad', 9542542542)


##

def person_details(name, **details):
    print(name)
    print(details)

person_details('Raja',age=16,city='Hyderabad', mobile=9542542542) ## once we provide the keyword here and run the program will get "person_details() got an unexpected keyword argument 'age' error then need to give "**" for function level arguments"

## Results:
Raja
{'age': 16, 'city': 'Hyderabad', 'mobile': 9542542542}


####

def person_details(name, **details):
    print(name)
    for i,j in details.items():
        print(i,j)

person_details('Raja',age=16,city='Hyderabad', mobile=9542542542)

##RESULTS 
Raja
age 16
city Hyderabad
mobile 9542542542




######## GLOBEL VS LOCAL VERIABLES ######

# Inside the function is the LOCAL veriable
# Out side the function is called GLOBEL veriable 

#using globel veriable in side the local
x = 10

def local():
    
    print('inside', x)

local()

print('outside',x)

#results:
>>> local()
inside 10
>>> print('outside',x)
outside 10



#using globel veriable & in side/local veriable seperately

x = 10

def local():
    x=500
    print('inside', x)
local()
print('out side', x)

#Results like below
>>> local()
inside 500
>>> print('out side', x)
out side 10
>>> 


# If we want to change the Globel veriable value as same local veriable

x = 10

def local():
    global x    # need to give this if we want to change the Globel veriable value as same local veriable
    x=500
    print('inside', x)
local()
print('out side', x)


##Results shows like below:

>>> local()
inside 500
>>> print('out side', x)
out side 500




