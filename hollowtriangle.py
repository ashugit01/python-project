n=8
for i in range(n):
    for j in range(i):
        if j==0 or i==n-1 or i-1==j :
                    print("*",end=" ")
        else:
                    print(" ",end=" ")
    print()        