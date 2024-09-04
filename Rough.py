
def add(a,b):
    print(a+b)

add(1,2)


def wish():
    print("hellow")

wish()

def wish(name):
    print('hellow {} good morning'.format(name))

wish("Raja")

def squire(number):
    print(number*number)

squire(4)



def squire(number):
    print('the number of {} squire is {}'.format(number, number*number ))

squire(4)


def add(a,b):
    print("The number of {}, number of {} sum is {}".format(a,b,a+b))

add(62,78)


def add(a,b):
    return(a*b)
add(5,6)


def evenorodd(a):
    if a%2==0:
        return("The provided number is a Even value")
    else:
        return("This is an odd value")

#evenorodd(6)
evenorodd(int(input("enter the value : ")))





def add(a,b):
    return(a*b)
result=add(5,6)
print("The sum of add is:", result)


def fact(n):
    result=1
    while n>1:
        result=result*n
        n=n-1
    return result
for i in range (1,10):
    print("factorial {} is {}".format(i,fact(i)))




def calc(a,b):
    sum = (a+b)
    sub = (a-b)
    div = (a/b)
    mul = (a*b)
    return (sum,sub,div,mul)

w,x,y,z = calc(10,20)
print(w)
print(x)
print(y)
print(z)


