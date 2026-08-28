import array
a = array.array('f', [1.0, 2.0, 3.0, 4.0, 5.0])
for i in a:
    print(i)


#user input program
import array
n=int(input())
a=array.array('i',[])
for i in range(n):
    val=int(input())
    a.append(val)
for i in a:
    print(i,end=" ") 







