

### Printing Patterns in Python ###

Q) Create a 4 #  in 4 Rows like below pattern

####
####
####
####

#Correct one
for i in range(4):
    for j in range(4):
        print("#", end="")
    print()



###The below one is another way

for j in range (4):
    print("#", end="")
print()
for j in range (4):
    print("#", end="")
print()
for j in range (4):
    print("#", end="")
print()
for j in range (4):
    print("#", end="")
print()


### to print below pattern

#
##
###
####

# telusko code

for i in range(4):
    for j in range(i+1):
        print("#", end="")
    print()


#Another own code example for above pattern

for i in range(1,5):
    for j in range(i):
        print("#", end="")
    print()






### to print below pattern

####
###
##
#

# Telusko
for i in range(4):
    for j in range(4-i):
        print("#", end="")
    print()

#own
for j in range(4):
    for i in range(4-j):
        print("#", end="")
    print()






### To apply "continue", "break" for above patterns

for i in range(4):
    if i==2:
            continue
    for j in range(4):      
        print("#",end="")
    print()

# here we have given break statement inside of the nested for loop hence when i==2 applied inner loop skip the 2### program excution has stopped. 

####
####

####

for i in range(4):
    for j in range(4):
        if i==2:
            break
        print("#",end="")
    print()
print("This is end")


# here we have given break statement out side of the nested for loop hence when i==2 applied end the statement and program excution has stopped. 
####
###

for j in range(4):
    if i==2:
            break  # here we have given break statement out side of the nested for loop hence when i==2 applied end the statement and program excution has stopped. 
    for i in range(4-j):
        print("#", end="")
    print()





for j in range(1,5):
    for i in range(j):
        print("*", end="")
        if i==2:
            break
    print()


