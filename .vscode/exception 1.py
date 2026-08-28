try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("error:can't divide by zero")
finally:
    print("exception completed")






#pgm2
try:
    a=int(input())
    b=int(input())
    print(a/b)
except ZeroDivisionError:
    print("error:can't divide by zero")
else:
    print("no error",a/b)
finally:
    print("exception completed")
