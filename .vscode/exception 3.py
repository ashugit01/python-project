#pgm 6
try:
    print(a)
except NameError:
    print("Error:variable is doesn't exist")
finally:
    print("it is a finally block")




#pgm 7
def check_score():
    try:
        print(score)
        score=48
    except UnboundLocalError:
        print("Error:you must assign the value first")
check_score()                                            