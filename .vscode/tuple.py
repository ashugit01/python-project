#add new value in tuple
t=(1,3,3,4)
print(t)
l=list(t)
l.append(5)
print(tuple(l))


#count occurance of a tuple
t1=(1,2,2,4,5)
print(t1.count(4))


#find index of a value
t1=(1,8,5,2,4)
print(t1.index(5))


#concotenation
t2=(1,2,3)
t3=(4,5,6)
print(t2+t3)


#repeat tuple
t4=(1,2,5)
print(t4*6)


#slicing a tuple
t5=(1,2,3,4,5)
print(t5[1:4])

#nested tuple access
t6=((1,2),(3,4),(5,6))
print(t6[1][1])
print(t6[2][0])

#max and min
t7=(1,3,2,6)
print(max(t7),min(t7))


#sorted tuple
t8=(4,5,61,0)
print(tuple(sorted(t8)))

#check membership
t9=("apple,orange,cherry")
print("cherry" in t9)

#sum of tuple
t10=(1,3,3,3)
print(sum(t10))


#swap to tuple
t11=(1,2)
t12=(3,4)
t11,t12=t12,t11
print(t11,t12)

#length of tuple
t12=(1,3,4,5)
print(len(t12))

#reverse tuple
t12=(1,3,4,5,6)
print(t12[::-1])