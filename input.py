
### if out of range by using FOR LOOP with "INPUT" value 

av=5
x=int(input("Enter how many items required :"))
i=1
while i<=x:
    #if i>av:
        #print(("Out of stock"))
        #break
    if x>av:
        print("These many items are not avilable in michene")
        break 
    print("Item :",i)
    i=i+1



