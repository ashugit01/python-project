#insert value in array
import array 
arr=array.array('i',[1,3,4,78,7])
arr.insert(3,5)
print(arr)       
#deletion in array
arr.remove(78)
print(arr)
#remove by index
arr.pop(1)
print(arr)
#remove last index value
arr.pop()
print(arr)



#count the occurance
b=array.array('i',[10,20,20,40,20])
count=b.count(20)
print(count)

#average of array elements
c=array.array('i',[1,2,3,4,5])
avg=sum(c)//len(c)
print(avg) 


#find max in array withour using built in method
import array
n=int(input())
a=array.array('i')
for i in range(n):
    data=int(input())
    a.append(data)
max=a[0]
for n in a:
    if n>max:
        max=n
print("maximum:",max)


#find min in array without using built in method
import array
n=int(input())
a=array.array('i')
for i in range(n):
    data=int(input())
    a.append(data)
min=a[0]
for n in a:
    if n<min:
        min=n
print("minimum:",min)







