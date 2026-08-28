import array
n=int(input())
a=array.array('i')
for i in range(n):
    val=int(input())
    a.append(val)
t=int(input("enter target value:"))
left=0
right=n-1
result=-1
while left<=right:
    mid=(left+right)//2
    if a[mid]==t:
        result=mid
        break
    elif a[mid]<t:
        left=mid+1
    else:
        right=mid-1

if result!=-1:
    print("element found at index:",result)
else:
    print("element not found")





#NEW
import array
a=array.array('i',[33,4,55,6,77])
t=7
left=0
right=len(a)-1
result=-1
while left<=right:
    mid=(left+right)//2
    if a[mid]==t:
        result=mid
        break
    elif a[mid]<t:
        left=mid+1
    elif a[mid]>t:
        right=mid-1
if result!=-1:
    print("element found at index:",result)
else:
    print("element not found")        
