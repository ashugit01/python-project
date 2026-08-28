a=[1,2,3]
b=[3,5,10]
print(sorted(a+b))


#max and min
l=[1,2,3,4,5]
print(max(l))
print(min(l))


#shuffling
import random
l=[50,2,30,1,40]
random.shuffle(l)
print(l)


#find  max and min without using builtin method
n=int(input("enter size of list"))
a=[]
for i in range(n):
    i=int(input())
    a.append(i)
large=a[0]
for i in a:
    if i>large:
        large=i
print(large)




