class a:
    def display(self):
        print("its displaying the class a")
class b(a):
    def display(self):
        print("its displaying the class b")
ob=b()
ob.display()