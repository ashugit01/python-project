import array
n=int(input("enter size of array:"))
a=array.array('i')
for i in range(n):
    val=int(input())
    a.append(val)
print("your array:",a)
for i in range(n):
    for j in range(i+1,n):
        min=i
        if a[j]<a[min]:
            min=j
        a[i],a[min]=a[min],a[i]
print("sorted array",a)

  