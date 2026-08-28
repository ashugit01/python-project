num1 = int(input())
num2 = int(input())
op = input()
if op=="+":
    print("result=",num1+num2)
elif op=="-":
    print("result=",num1-num2)
elif op=="*":
    print("result=",num1*num2)
elif op=="/":
    if num2 !=0:
      print("result=",num1/num2)
    else:
        print("division by zero is not allowed")

else:
    print("invalid operator")


