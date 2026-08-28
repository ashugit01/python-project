#sum of list
n=int(input())
a=[]

for i in range(n):
    i=int(input())
    a.append(i)

sum=0

for i in a:
    sum+=i

print(sum)