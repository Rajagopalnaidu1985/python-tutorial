

#### LOOPS #####


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

-----
i=1
while i<=5:
    print(i)
    i=i+1

i=1
while i<=20:
    print(i)
    i=i+1
        
        

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


##3 NAME RAJAGOPALNAIDU with while loop ###
i=1  
while i<=3:  
    print(i, "Raja", end="")
    j=1
    while(j<=1):
        print("Gopal", end="")
        k=1
        while(k<=1):
            print("naidu", end="")
            k=k+1
        j=j+1 
    i=i+1 
    print()








#### For loop ########

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

#
for i in range(1,10):
    if i%2!=0:
        print(i)     # 2 divisables are not displayed


#
for i in range(1,10):
    if i%2==0:
        print(i)     # 2 divisables only will display


#

for i in range (41,20,-2):
    print(i)


###### NESTED FOR LOOP#####

for i in range(1,100):
    if i%3!=0:
        if i%5!=0:
            print(i)

### Above Same query we can write as below:

for i in range(1,50):
    if i%3!=0 and i%5!=0:
        print(i) 


### by using or both divisable values will not display
for i in range(1,61):
    if i%3!=0 or i%5!=0:
        print(i) # from this out put 15,30,45,60 will be missing as these nubers will divisible by both 3, 5


for i in range(1,61):
    if i%3==0 and i%5==0:
        print(i) # will display 15,30,45,60 these nubers only as these will divisible by both 3, 5


for i in range(1,61):
    if i%3==0 or i%5==0:
        print(i) #3,5 both divisible numbers will dislay














############ Key words "break", "Continue", "Pass" ###########

# 1) Break
# 2) Continue
# 3) Pass

# 1) Break

while using wending michene if we try to enter morethen avilable items in the mechene then 

# if with in range by using FOR LOOP

for i in range(5):
    if i>=10:
        print("Given count is out of range")
        break
    print(i)


# # if out of range by using FOR LOOP

for i in range(11):
    if i<10:
        print("Given count is out of range")
        break
    print(i)


### if with in range by using WHILE LOOP (with out "input" option)
#ex: wending mechene has 3 items only but upto 5 items that will give so 
# if customer enter/looking for 5 items from the mechene, will give 3 items and for 4th system will diplay not avilable message 

av=3    ## av = avilability 
i=1
while i<=5:
    if i>av:
        print("Input items are not avilable in the mechene")
        break
    print(i)
    i+=1  # 3 items will get but for 4th item will display "Input items are not avilable in the mechene" message
    




##### To run same queries by using same WHILE & FOR LOOPS #####

for i in range(31):
    if i%3!=0:  #divisible by 3 number are not displayed from the results
        print(i)

for i in range(1,31):
    if i%3==0:  #divisible by 3 number will displayed from the results
        print(i)

#Reverse for above

for i in range(31,1,-1):
    if i%3==0:  #divisible by 3 number will displayed from the results
        print(i)


##Same testing using while loop

i=1
while i<=30:
    if i%3!=0: # Except divisible 3 numbers remining will display
        print(i)
    i=i+1

#Reverse order

i=30
while i>=1:
    if i%3==0: #all 3 divisible numbers will display
        print(i)
    i=i-1
    




### if out of range by using FOR LOOP with "INPUT" value 

av=5
x=int(input("Enter how many items required :"))
i=1
while i<=x:
    #if i>av: ### if user enter morethen avilable items with this condition michene will provide avilable items in the michene and will give below mentioned error message.
        #print(("Out of stock"))
        #break
    if x>av:  ### with this condition michene will not provide any item if user enter morethen avilable items and stright away will give below mentioned error message.
        print("These many items are not avilable in michene")
        break 
    print("Item :",i)
    i=i+1    






# 2) Continue

for i in range(1,31):
    if i%3!=0 and i%5!=0:  #divisible by 3,5 number will displayed from the results
        continue
    print(i)
print("Done")

for i in range(1,31):
    if i%3!=0 or i%5!=0:  #will displayed divisible by both 3 & 5 numbers only in result
        continue
    print(i)
print("Done")

for i in range(1,11):
    if i%3==0 or i%5==0:  #divisible by 3 & 5 numbers will not displayed from the results
            continue
    print(i)
print("Done")


#Reverse for above

for i in range(31,1,-1):
    if i%3==0:  #divisible by 3 number will displayed from the results
        print(i)
        if i<3:
            continue
print("this is end")


##Same testing using while loop

i=1
while i<=30:
    if i%3!=0: # Except divisible 3 numbers remining will display
        print(i)
    i=i+1
    if i>30:
        continue
print("Done with the 3rd table")    

#Reverse order

i=30
while i>=3:
    if i%3==0: #all 3 divisible numbers will display
        print(i)
    i=i-1
    if i<3:
        print("No 3 divisibls after this number")
    continue

    


## 3) Pass ##

#where which we don't need to print odd numbers between 1 - 100

for i in range (1,100):
    if i%2==0:
        pass
    else:
        print(i)
print("above list is odd values between 1 to 100")
        


for i in range (1,20):
    if i%2!=0:
        continue
    else: 
        print(i)


for i in range (1,21):
    if i%10!=0:
        break
    else: 
        print(i)
print("Myavvv")
    




