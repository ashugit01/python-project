# basic syntax
d={"a":1 ,"b":2} #a,b=keys 1,2=value


#empty dictionary
d1={}
print(d)
print(d1)

#adding and updating new value
d2={}
d2["yes"]=1
d2["no"]=2
print(d2)


#accesing value in dict
d3={"red":4,"black":7}
print(d3["red"])
print(d3["black"])

#get method()
d4={"apple":7,"cherry":8,"berry":9}
print(d4.get("cherry"))
print(d4.get("banana"))


#check key is exist
d4={"apple":7,"cherry":8,"berry":9}
print("apple" in d4)

#looping in dict
d4={"apple":7,"cherry":8,"berry":9}
for value in d4.values():
    print(value)
for key in d4 :
    print(key)
for key,value in d4.items():
    print(key,value)


#count letters in word
word="apple"
count={}
for ch in word:
    count[ch]=count.get(ch,0)+1
print(count)

#find sum of all dict value
d5={"a":1,"b":2,"c":3,"d":4}
print(sum(d5.values()))
print(d5.values())
print(d5.keys())


#sorted in dict
d6={"c":-1,"a":5,"b":0}
print(dict(sorted(d6.items())))


#merge two dict
d7={"a":28}
d8={"b":9}
d7.update(d8)
print(d7)


#create dict for two list
keys=["a","b","c",]
values=[1,3,7]
print(dict(zip(keys,values)))


#check two dict are equal
d7={"a":1,"b":2}
d8={"b":2,"a":1}
print(d7==d8)


#find min value in dict
d9={"b":2,"a":1,"c":-4}
print(min(d9,key=d9.get))

#total number of keys in dict
d10={"a":5,"b":4,"c":9}
print(len(d10))

#common keys and values between two dict
d11={"a":10,"b":5}
d12={"t":10,"b":53}
print(set(d11.keys())&set(d12.keys()))
print(set(d11.values())&set(d12.values()))


#convert dict to list of tuple
d13={"a":1,"b":2}
print(list(d13.items()))


#copy a dict
d13={"a":1,"b":2}
d14=d13.copy()
d14["c"]=9
print(d14)


#only unique values
d15={"a":4,"b":6,"c":4,"e":3}
print(set(d15.values()))


      



