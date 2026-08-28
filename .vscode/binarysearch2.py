import array
a=array.array('i',[1,2,3,4,5,6,7])
t=3
left=0  #0 ,#2
right=len(a)-1 #6, #2
found=-1
while left<=right:
    mid=(left+right)//2 #3, #1 ,#2
    if a[mid]==t: #4==3,#2==3,#3==3
        found=mid
        break
    elif a[mid]<t:#4<3,#2<3
        left=mid+1 #1+1=2
    elif a[mid]>t:#4>3
        right=mid-1 #3-1=2
if found!=-1:
    print("element found at index:",found)
else:
    print("element not found")