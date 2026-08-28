#string concatenation
s1="good"
s2="morning"
s3=s1+ " " + s2
print(s3)




#string repetition
a="hello"
print(a*3)




#string indexing
name="python"
print(name[0])
print(name[-1])
print(name[:])




#slicing
name="ashini"
print(name[0:4])





#string searching
name="ashini is fine"
print(name.find("r"))


name="ashini is fine"
print(name.index("f"))




#string searching
s="apple"
print("app" in s)
print(s.count("p"))


#string manipulation
s="ashini dass"
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.swapcase())



#strip
s="Apple"
print(s.strip())
print(s.lstrip())
print(s.rstrip())


#replace
A="i like vegess"
print(A.replace("vegess","fruits"))



#split method
#split string into list
s="apple,orange,grape"
fruits=s.split()
joined="_".join(s)
print(joined)


#checking string using is methods
print("123k".isdigit())
print("ashini".isalpha())
print("123abc".isalnum())
print("4".isspace())



#startswith and endswith
s="velankanni"
print(s.startswith("vela"))
print(s.endswith("in"))









