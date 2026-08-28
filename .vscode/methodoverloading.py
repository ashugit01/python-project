def add(a,b,c=0):
    print(a+b+c)
add(3,5)
add(3,5,6)

#eg;
def sub(a,b,c=0):
    print(a-b-c)
sub(3,4)
sub(4,5,6)

#methodoverloading eg:
def max(a,b,c=0):
    if a>b and a>c:
        print(a,"is max")
    elif b>c and b>a:
        print(b,"is max")
    else:
        print(c,"is max")
max(13,24,21)
max(13,43)