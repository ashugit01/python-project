#linear search
import array
n=int(input())
a=array.array('i')                                                                                                                                                                                    
for i in range(n):
    val=int(input())
    a.append(val)
target=int(input("Enter the target value: "))
found=-1
for i in range(len(a)):
    if a[i]==target:
        found=i
        break
if found!=-1:
    print("element found at index:",found)
else:
    print("element not found")    