#pgm 3
try:
    a=int(input())
    b=int(input())
    print(a/b)
except ValueError:
    print("error:invalid input")
except ZeroDivisionError:
    print("error:can't divide by zero")
else:
    print("no error",a/b)
finally:
    print("exception completed")








#pgm 4
try:
    a=[1,3,5,6,7,8,9]
    print(a[5])
except IndexError:
    print("Error:can't find this index")
else:
    print("no error",a[5])
finally:
    print("exception completed")






#pgm 5
try:
    dict={"berry":1,"cherry":2}
    print(dict["kiwi"])
except KeyError:
    print("Error:can't find this key")
finally:
    print("it is a finally block")







