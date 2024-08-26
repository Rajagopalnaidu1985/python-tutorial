


###

s = "ABCDEFGHIJ"

s[1:6:2]  #--> forword direction , from begin to end -1 (1 to 5)
s[::1]    #--> Complete string in original order






[::-1]   #--> Complete string in  reverse order
s[3:7: -1]  #--> Backward direction, from beagin to end +1 (3 to 8)
s[7:4:-1]  #--> Backward direction, from beagin to end +1 (7 to 5)
s[0:1000000:1] #--> complete string in same order
s[0:1000000:-1] #--> Backward direction, from 0 to 1000001 (will get Empty string)
s[-4:1:-1] #--> Backward direction begain to end +1 which means -4 to 2

s[5:0:1] #--> end value is 0 hence we will get empty string
s[9:0:0] #--> will get error as increament/step value is 0
s[0:-10:-1] #---> Empty string we will get








#### MATHEMATICAL OPERATORS FOR STRING #####

+
*


## When we use + operators both String orguments should be in STRING only.
## if one is string another one is ny other type this will not work 

str+str

## When we use * operator which is String repitation operator. Below both scenarios are acceptable

str * int
int * str

Examples:

s = ["Raja" + "Gopal" + "Naidu"]
print(s)

string = ["Raja" * 3]
print(string)




s=input("enter any string")
print('in forward direction:')
i=0
while i<len(s):
    print(s[i])
    i=i+1




### other way

s=("INDIA")
print('s')
i=0
while i<len(s):
    print(s[i])
    i=i+1

print("s")
i=-1
while i>= -len(s):
    print(s[i])
    i=i-1



### Memebership operaters ###

--> in,
--> not in,

s = "maintence"

print('i' in s)
print("K" in s)
print('C' in s)
print('z' not in s)
print('a' not in s)











print('in forward direction:')



## Comparison between strings ###

#S1=input("First string value")
#S2=input("Second string value")


S1="Raja"
S2="Saja"
if S1 == S2:
    print('Both values are equeal')
elif S1 < S2:
    print('S1 is lessthen the S2')
else:
    print('S1 is graterthen the S2 value')


### Remove spaces from the Strings ###

rstrip() --> To remove spaces from right hand side for the string (End of string)
lstrip() --> To remove spaces from left hand side for the string (Beginning of the string)
strip() ---> To remove spaces for both sides from the string



###problem is: How to remove Spaces from string 

city=input("Enter your city name: ").lower.strip
if city == 'Hyderabad':
    print("Hellow Hyderabad...Good Morning!!!")
elif city == 'Chennai':
    print("Hellow Chennai...Good Morning!!!")
elif city == "Delhi":
    print("Hellow Delhi...Good Morning!!!")
else:
    print("Given input is not in range")


