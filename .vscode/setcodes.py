l=[1,2,4,5]
print(set(l))

#add multiple value to a set
s1={1,2,3}
s1.update([4,5,6])
print(s1)


#remove value from a set
s2={1,2,3,4}
s2.discard(3)
print(s2)



#check two sets are disjoint
s3={1,2,3,4}
s4={4,5,6,7,8}
print(s3.isdisjoint(s4))


#subset and superset
s5={1,2}     #subset
s6={1,2,3,4}    #superset
print(s5.issubset(s6))
print(s6.issuperset(s5))


#find unique words from two sentences
s7="i love briyani"
s8="i love curdrice"
print(set(s7.split())^set(s8.split()))


#shallow copy
s8={1,2,3}
s9=s8.copy()
s9.add(4)
print(s9)



#sort the set
s10={1,0,9,3}
print(set(sorted(s10)))


#find common letter between two words
s11="hello"
s12="world"
print(set(s11)&set(s12))


#clear all the elements from the set
s13={1,3,4,5}
s13.clear()
print(s13)


#remove duplicates
s14={1,2,3,5,6,3,2,1}
print(s14)

#frozenset
s15=frozenset([1,2,3,4])
print(s15)

#union
a,b,c={1,2},{3,4},{5,6}
print(a.union(b,c))


#check particular element
s16={"apple","orange","berry"}
print("apple" in s16 )


#intersection update
s17={1,2,3,4}
s18={2,3,5,6}
s17.intersection_update(s18)
print(s17)



#count unique elements
list=[1,3,3,1,4,5,2,5,6]
print(len(set(list)))

#set equality check
s19={1,2,3}
s20={2,1,3}
print(s19==s20)