


def count(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            print(i)
            i=i+1
        else:
            print(i)
            i=i+1
    return even,odd

lsist = [2,5,7,43,67,88,65,45,62,84]

even, odd = count(list)
print(even)
print(odd)

