

####### TYPES OF ARGUMENTS / PARAMETERS #######


def f1(a,b): #arguments/parameters  
    pass

f1(10,20) #arguments



##### TYPES OF ARGUMENTS / PARAMETERS #####

4 types of ARGUMENTS / PARAMETERS


1) Positional argumnets
2) Key word arguments 
3) Default arguments
4) Veriable lenght arguments



### 1) Positional argumnets ####

def sub(a,b): 
    print(a+b)  # positional argumments, The number of arguments should be match with paraments


### 2) Key word arguments ####

def sub(name,DOB, age): 
    print(name="RAJA", DOB="02-02-1985", age="35") # here "name" is key word "RAJA" is a value of that argument



### 3) Default arguments ####

def wish (name="gust"):
    print("Hellow", name, "Good morning!!!")

wish() # Hellow gust Good morning!!!
wish("Raja") #Hellow Raja Good morning!!!

# Default arguments should be last arguments, i.e after default argumnets we can't take non default arguments.



### 4) Variable lenght arguments ####




