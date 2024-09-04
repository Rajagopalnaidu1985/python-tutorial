

### Contienue - will skip the perticulor itresion and print remining values 
# Example 

for i in range(5):
    if i==3:
        continue # here 3 will not disply in the results
    print(i) 


#Ex2:

for i in range (20):
    if i%2==0:
        continue #All 2 divisible values are not display from the results
    print(i)


### Break ###

## Break -  Break will stop the loop and display the results

#Example

for i in range(5):
    if i==3:
        break #in this loop to print the 0 to 5 values in results when 3 will be i value loop will break and 4,5 will not print in the results
    print(i)

#Ex2:

for i in range(1,31):
    if i%3==0:
        break #in the loop asper if statement 3 divisible numbers should display but due to Break when i value became 3 and it is divisible by 3 so that loop has stopd so results are only 1,2
    print(i)


for i in range(1,31):
    if i%15==0:
        break #in the loop asper if statement 15 divisible numbers should display but due to Break when i value became 15 and it is divisible by 15 so that loop has stopd so results are upto 14 numbers
    print(i)



### Pass ###

#Pass: While define a funcation/class and if we don't have clarity to define it then we can use Pass to skip that at that moment.

def fun():
    pass
a = 5

#same applicable for class also

class human:
    pass


