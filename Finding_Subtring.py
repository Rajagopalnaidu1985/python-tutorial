

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






