# 2024-08-21

# Functions:
1. Inbult functioins
    id()
    print()
    input()
    eval()
    len()

2. Userdefine Functions
If pre defined functions are not fullfill our code requirements then we can make user defined 
functions 

Syntax for userdefined function:
    
def function_name(Paratmeters --> example a,b):
    "if requre doc string enter"
    business logic (10,20 --> example "Arguments" )
    business logic
    business logic
    business logic
    Return Value

*** here paramater/arguments are Input for the function & return is the Output of the function


#DEFINE A FUNCTION to print Hellow:

def whish():
    print("Hellow")

#CALLING A FUNCTION:

whish()   

*** if a function contains Parameters, at the time of calling the function we should provide the 
values otherwise will get error.

#example write a function with parameter by calling the name

def wish(name):
    print('Hellow {},Good Morning!!'.format(name))

wish('Rajagopal') 

name = input('Enter name:')
wish(name)


def squireit(num):
    print(num, num**2)

squireit(2)
squireit(3)
squireit(5)
squireit(6)



def add(x,y):
    print("The sum of {} and {} is : {}" .format(x,y,x+y))

add(2,4)
add(3,10)
add(5,13)
add(60,86)









a = 20
b = 30
print ('The sum of:', a+b)
print ('The difference of:', a-b)
print ('The mutiplication of:', a*b)


def math (a,b):
    print ('The sum of:', a+b)
    print ('The difference of:', a-b)
    print ('The mutiplication of:', a*b)
    print ('The division:', a/b)
math(200,100)
math(40,60)





#TETURN STATEMENT:

def add(x,y):
    return(x+y)
result = add(12,23)
print(result)

#
def add(x,y):
    return(x+y)
result = add(12,23)


##
def f1():
    print('Hellow')
result = f1()
print(result)


## write a function either given number is Even number or Odd?

def even_odd(x):
    if x%2==0:
        print('It is even number')
    else:
        print('It is a odd number')

even_odd(int(input("enter any number to check the results")))

#
def even_odd(x):
    if x%2==0:
        return 'It is even number'
    else:
        return 'It is a odd number'
result = even_odd(20)
print(result)


###
def show(sequence):
    for x in sequence:
        print(x)

print(show)
show("Rajagopal")
show(range(0, 10))

### Write a function to find a factorial of given number???

def fact(n):
    result = 1 
    while n > 1:
        result = result * n
        n = n - 1
        return result
    
print(fact(5))



##
def fact(n):
    result=1 
    while n>1:
        result=result*n
        n=n-1
        return result
for i in range(1,11):
    print('The factorial of {} is :{}'.format(i,fact(i))) 



def fact(n):
    result = 1
    while n > 1:
        result = result * n
        n = n - 1
    return result

print(fact(5))