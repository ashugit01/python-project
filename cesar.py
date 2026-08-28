text=input("enter a word:")
shift=4
result=" "
for i in text:
    result=result+chr(ord(i)+shift)
print("encrypted text:",result)
