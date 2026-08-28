import array
n=int(input())
a=array.array('i')
for i in range(n):
    val=int(input())
    a.append(val)
for i in range(n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)