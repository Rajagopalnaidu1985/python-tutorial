
String data type:

1. Any sequence of charcaters we can call it as string
2. We can mention this data type in "Single quote / Double quotes / Trple quotes"
3. here we can use triple quotes when we are writing Multy line literals
     
example: 
name = "Raja
gopal
Naidu"  

print(name) #Error

Name = '''Raja
gopal
Naidu''' #Success



How to access characters in the string:

1. By using Indexing
2. By using Slice operater

s = 'raja'
print(s[2])
print(s[-2])
print(len(s))

Ex: Write a program to read string from the key board and display 
its characters by index wise (both positive and negative index wise)

##Positive index 

s = 'raja'
i=0
for x in s:
    print('The chracter of positive index {} is {}' .format(i,x))
    i=i+1

## Negative index

s = 'raja'
i=-1
for x in s:
    print('The chracter of positive index {} is {}' .format(i,x))
    i=i-1

## or if we need both indexes in one line

s = 'raja'
i=0
for x in s:
    print('The chracter of positive index {} and negative index {} is {}' .format(i,i-len(s),x))
    i=i+1


##another example:

s = 'DEVARA'
i=0
for x in s:
    print('The chracter of positive index {} and negative index {} is {}' .format(i,i-len(s),x))
    i=i+1




s = "RAMAMMM RAGAVAM"
i=0
for x in s:
    print("Positive index is {} Negative index is {} letter is{}" .format(i,i-len(s),x))
    i=i+1


s = "RAMAMMM RAGAVAM"
i=0
for x in s:
    print(x)
    i=i+1
print(i)



#### Indexing by using Slice operater:

Slice operater syntax = [Begain value : End value : Step value]

slice operater won't rise index error



string = "0123456789012345"
print(string[2:100])
print(string[3:7])


Slice [Begin value : End value : Step value ]
All atributes are optional in slicing 
All values can be either +ve or -ValueError

if step value is +ve then forword direction from Beagin to End-1
if step value is -ve then Backward direction from End to Beagin +1 

In forward direction if End value is "0" the result is always Emply string
In the Backward direction if the end value is -1 then result is always Empty string


