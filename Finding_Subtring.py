

Finding substrings :


## 1) find()
## 2) index()

# 3) rfind
# 4) rindex


## FIND , RFIND: will search complete string until finding first occurrence in forword direction 

#string.find(substring)
#Returns - Index of first occurrence of the given substring
#Returns - '-1' if that perticulor sub string is not avilable in the string 

#find (substring,begin, end) --> Which means beagin begain to end -1


##Example

s='Learning python is very importent in programing & python is easy to learn.'
print(s.find('python'))
print(s.rfind('python'))
print(s.find('name'))
print(s.find('e',0,9)) #here 0,9 are indicates indexation values so 'e' avilable in the range hence return the value
print(s.find('l',1,9)) #here 0,9 are indicates indexation values so 'L' is not avilable in the range hence return -1
print(s.rfind('l'))
print(s.rfind('z'))
print(s.find('z'))


## index() is exactly same as find() method except that if the specified substring is not avilable then we will get value Error
 

s='Learning python is very importent in programing & python is easy to learn.'
print(s.find('python'))
print(s.index('python'))
print(s.rfind('python'))
print(s.rindex('python'))
print(s.find('name'))
print(s.index('name'))
print(s.find('e',0,9)) #here 0,9 are indicates indexation values so 'e' avilable in the range hence return the value
print(s.index('e',0,9))
print(s.find('l',1,9)) #here 0,9 are indicates indexation values so 'L' is not avilable in the range hence return -1
print(s.index('l',1,9))
print(s.rfind('l'))
print(s.rindex('l'))
print(s.rfind('z'))
print(s.rindex('z'))
print(s.find('z'))
print(s.index('z'))


#### Write a program to Display all positions of substring in the given main string
# s=input('enter main string)
# substring=input('enter substring)


s='Learning python is very importent in programing & python is easy to learn.'
substring = 'python'
print(s.find_all_occurrences(s,substring))




### While Loop
Having below 3 parts
1) #Initialisation / Assign the value
2) #Condition
3) #Increment/Decrement




i=1  #Initialisation 
while i<=5:  #Condition
    print("Raja",i) 
    i=i+1 #Increment/Decrement

## reverse while loop

i=10
while i>=1:
    print("Mango",i)
    i=i-1

## nested while loop

i=1  
while i<=5:  
    print(i, "Raja", end="")
    j=1
    while(j<=3):
        print("Gopal", end="")
        j=j+1 
    i=i+1 
    print()


#Example
i=1
while i<=5:
    print(i,"Raja : ", end="")
    j=1
    while j<=5:
        print(j,"Monkey, ",end="")
        j=j+1    
    i=i+1
    print()

#Example

i=1
while i<=5:
    print(i,"Man: ",end="")
    j=1
    while j<=5:
        print("Monkey",j,"; " , end="")
        j=j+1
    i=i+1
    print()




### For loop

##String
s = "RAJAGOPALNAIDU"
for i in s:
    print(i) # this code will provide each "i" value in seperate lines



#to retrive above string results in a single line

s = "RAJAGOPALNAIDU"
for i in s:
    print(i,end="")
     


## For loop with "List":
##LIST

l=["Raja", 99, 99, 8.7] # this list is having str,int,flot
for i in l:
    print(i)


## For loop with "Tuple":
##Tuple

t=(1,2,2,3,4,6,7,8)
for i in t:
    print(i)


T=(11)
for i in range(T):
    print(i)



for i in range(23,37): # here range starting value consider as 23 and end value is n-1 which is 37-1=36
    print(i)
    
for i in range(1, 50, 5): # Here 1 is starting value, 50-1 is ending value & 5 is itreation (difference) which means every 5th number will be in results
    print (i)    

#reverse
for i in range(11,0,-2):
    print(i)


## which we don't want to print the values are Divisible by 5

for i in range(1,50):
    if i%5!=0:
        print(i) # if you observe this results 5 divisible numbers will not display means 5,10,15,20,25........


for i in range(1,10):
    if i%2!=0:
        print(i)     # 2 divisables are not displayed



for i in range(1,10):
    if i%2==0:
        print(i)     # 2 divisables only will display




