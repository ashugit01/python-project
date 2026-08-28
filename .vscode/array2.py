#sum of all elements in array
import array
a=array.array('i',[3,4,5,8,7])
sum=0
for i in a:
    sum+=i
print(sum)



#sum of all elements
import array
n=int(input())
a=array.array('i')
for i in range(n):
    data=int(input())
    a.append(data)
sum=0
for i in a:
    sum+=i
print(sum)  



